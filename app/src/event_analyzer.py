from collections import Counter
from typing import List
from .models import Joiner, Event

class EventAnalyzer:
    
    @staticmethod
    def get_joiners_multiple_meetings(events: List[Event]) -> List[Joiner]:
        all_joiners = []
        for event in events:
            all_joiners.extend(event.joiners)
        joiner_count = Counter(joiner.name for joiner in all_joiners)
        joiners_multiple_meetings = [
            joiner for joiner in all_joiners if joiner_count[joiner.name] > 1
        ]
        unique_joiners = list({joiner.name: joiner for joiner in joiners_multiple_meetings}.values()) 
        return unique_joiners
