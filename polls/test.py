#! python3
# Author: George Gao, gaojz017@163.com

import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_quesiton(self):
        """
        was_publisted_recently() returns False for questions whose pub_date is in the future.
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
