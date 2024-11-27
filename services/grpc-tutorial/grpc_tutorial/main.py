import article_pb2_grpc
import article_pb2
import grpc
from concurrent.futures import ThreadPoolExecutor


class ArticleServer(article_pb2_grpc.ArticleServiceServicer):
    def ArticleList(self, request, context):
        page = request.page
        page_size = request.page_size
        print(f"page: {page}, page_size: {page_size}")

        # Create response
        response = article_pb2.ArticleListResponse()
        articles = [
            article_pb2.Article(id=100, title="xx", content="yy", create_time="2030-10-10"),
            article_pb2.Article(id=101, title="11", content="22", create_time="2030-10-10"),
        ]
        response.articles.extend(articles)
        return response


def main():
    # 1. Create a grpc server
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    # 2. Add article service server to the server
    article_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleServer(), server)
    # 3. Bind server ip and port, insecure is sufficient for dev env
    server.add_insecure_port("0.0.0.0:5000")
    # 4. Start server
    server.start()
    print("Server has started!")
    # 5. Wait for termination
    server.wait_for_termination()


if __name__ == '__main__':
    main()