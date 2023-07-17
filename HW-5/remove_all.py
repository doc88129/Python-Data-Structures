from list_node import *


def remove_all(head, value):
  head = ListNode("dummy", head)
  tmp = head

  if not tmp:
    return None

  while tmp.next:
    if tmp.next.val == value:
      if not tmp.next.next:
        tmp.next = None
      else:
        tmp.next = tmp.next.next
    elif tmp.next:
      tmp = tmp.next
      pretty_print(tmp)

  return head.next


#pretty_print(remove_all(head_from_list([1,3,2,3,5]),3))
#pretty_print(remove_all(head_from_list([1,3,2,3,5]),1))
#pretty_print(remove_all(head_from_list([1,1,1,1]),1))
#pretty_print(remove_all(head_from_list([1,1]),1))
