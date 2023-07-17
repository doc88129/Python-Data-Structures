class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def pretty_print(head):
  temp = head
  while temp:
    if temp.next:
      print(temp.val, end=' -> ')
    else:
      print(temp.val)
    temp = temp.next


def head_from_list(lst):
  if not lst:
    return None

  head = ListNode(lst[0], None)

  temp = None
  prev = head

  for i in range(1, len(lst)):
    val = lst[i]
    temp = ListNode(val, None)
    prev.next = temp
    prev = temp

  return head