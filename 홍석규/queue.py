from typing import Any

class FixedQueue:
    class Empty(Exception):
        '''비어 있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외처리'''
        pass
    class Full(Exception):
        '''가득 차 있는 FixedQueue에서 인튜 할때 내보내는 예외처리'''
        pass

    def __init__(self, capacity: int) -> None:
        '''큐 초기화'''
        self.no = 0 # 현재 데이터 개수
        self.front = 0 # 맨 앞쪽 커서
        self.rear = 0 # 맨 끝쪽 커서
        self.capacity = capacity # 큐의 크기
        self.que = [None]* capacity # 큐의 본체

    def __len__(self) -> int:
        '''큐에 있는 모든 데이터 개수를 반환'''
        return self.no

    def is_empty(self) -> bool:
        '''큐가 디어 있는지 판단'''
        return self.no <= 0

    def is_full(self) -> bool:
        '''큐가 가득 차 있는지 판단'''
        return self.no >= self.capacity