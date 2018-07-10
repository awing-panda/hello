
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

from utils.user_agent import random_agent

# 主仆
class RandomUserAgent(UserAgentMiddleware):

    def process_request(self, request, spider):
        user_agent = random_agent()
        request.headers.setdefault('User-Agent', user_agent)
