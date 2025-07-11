from typing import List
import heapq

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort() 
        room_meet_count = [0] * n 

        available_rooms = list(range(n)) 
        heapq.heapify(available_rooms)

        ongoing_meetings = [] 

        for start, end in meetings:
          
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                end_time, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
            else:
                soonest_end, room = heapq.heappop(ongoing_meetings)
                delay = end - start
                new_end = soonest_end + delay
                heapq.heappush(ongoing_meetings, (new_end, room))
            room_meet_count[room] += 1

        max_meetings = max(room_meet_count)
        for i in range(n):
            if room_meet_count[i] == max_meetings:
                return i
