from rest_framework.pagination import LimitOffsetPagination

DEFAULT_SIZE = 50


class SizeOffsetPagination(LimitOffsetPagination):
    default_limit = DEFAULT_SIZE
    limit_query_param = 'size'
    max_limit = 300
