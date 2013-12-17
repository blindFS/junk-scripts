#!/bin/env python2
import sys
from python_simsimi import SimSimi
from python_simsimi.language_codes import LC_ENGLISH
from python_simsimi.simsimi import SimSimiException

simSimi = SimSimi(
    conversation_language=LC_ENGLISH,
    conversation_key='8bae6b81-536a-469d-a1ad-bbf141a3bd43'
)

try:
    response = simSimi.getConversation(' '.join(sys.argv[1:]))
    print(response['response'])
except SimSimiException as e:
    print(e)
