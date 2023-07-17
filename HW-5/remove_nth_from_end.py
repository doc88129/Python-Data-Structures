from list_node import *


def remove_nth_from_end(head, n):
  fast_point = head
  slow_point = head
  count = 0

  if not head:
    return None

  while fast_point.next:
    if count >= n:
      slow_point = slow_point.next
    count += 1
    fast_point = fast_point.next

  if slow_point == head or fast_point == slow_point:
    if count + 1 == n:
      return head.next
    return head

  if slow_point.next.next:
    slow_point.next = slow_point.next.next
  else:
    slow_point.next = None

  return head


#pretty_print(remove_nth_from_end(head_from_list([1,3,2,3,5]),1)) #1->3->2->3
#pretty_print(remove_nth_from_end(head_from_list([1,3,2,3,5]),2)) #1->3->2->5
#pretty_print(remove_nth_from_end(head_from_list([1,3,2,3,5]),5)) #3->2->3->5
