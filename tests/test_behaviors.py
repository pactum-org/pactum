import pytest

from pactum.behaviors import Notification


def test_basic_notification_behavior():
    behavior = Notification(target='arn:aws:sns:ap-south-1:123456789:behavior_test_executed')

    assert behavior.target == 'arn:aws:sns:ap-south-1:123456789:behavior_test_executed'


def test_notification_behavior_class_definition():
    class MyNotification(Notification):
        target = 'arn:aws:sns:ap-south-1:123456789:behavior_test_executed'

    behavior = MyNotification()

    assert behavior.target == 'arn:aws:sns:ap-south-1:123456789:behavior_test_executed'


def test_error_missing_target_attribute_on_notification_behavior():
    with pytest.raises(TypeError):
        Notification()
