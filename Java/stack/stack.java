
/**
 * Write a description of class Stack here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Stack
{
   
private Node head;  //Head of list that
//holds the Stack
public void push(Object x) 
{ head = new Node(x, head);
 }
 
public Object pop() {
  Node temp = head;
  head = head.next;
  return temp.data;
}

public Object peek() 
{ return head.data; 
}

public boolean isEmpty()
 { return head == null;
 }
    
public void clear() { head = null; }
}
