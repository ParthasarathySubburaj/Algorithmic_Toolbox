# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque(maxlen=self.size)
        self.last_finish_time = 0
        self.time = 0
    def process(self, request):
        arrival_time = request.arrived_at
        processing_time = request.time_to_process
        while self.finish_time:
            try:
                self.last_finish_time = self.finish_time.popleft()
                if self.last_finish_time > arrival_time:
                    self.finish_time.appendleft(self.last_finish_time)
                    self.time = self.finish_time[-1]
                    break
            except IndexError:
                pass
        if len(self.finish_time)< self.size:
            start_time = max(self.time, arrival_time)
            self.finish_time.append(start_time + processing_time)
            return Response(False, start_time)
        return Response(True, -1)  


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses  


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
