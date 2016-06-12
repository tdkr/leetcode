using System.Collections.Generic;

public class LRUCache
{
    int capacity = 0;
    Dictionary<int, int> valueDic = new Dictionary<int, int>();
    Dictionary<int, LinkedListNode<int>> nodeDic = new Dictionary<int, LinkedListNode<int>>();

    LinkedList<int> usedKeyList = new LinkedList<int>();

    public LRUCache(int capacity)
    {
        this.capacity = capacity;
    }

    public int Get(int key)
    {
        if (valueDic.ContainsKey(key))
        {
            LinkedListNode<int> node = nodeDic[key];
            usedKeyList.Remove(node);
            usedKeyList.AddFirst(node);

            return valueDic[key];
        }
        return -1;
    }

    public void Set(int key, int value)
    {
        if (valueDic.ContainsKey(key))
        {
            valueDic[key] = value;
            
            LinkedListNode<int> node = nodeDic[key];
            usedKeyList.Remove(node);
            usedKeyList.AddFirst(node);
        }
        else
        {
            if (valueDic.Count >= capacity)
            {
                int removeKey = usedKeyList.Last.Value;
                LinkedListNode<int> removeNode = nodeDic[removeKey];

                valueDic.Remove(removeKey);
                nodeDic.Remove(removeKey);
                usedKeyList.Remove(removeNode);
            }

            valueDic.Add(key, value);

            LinkedListNode<int> node = new LinkedListNode<int>(key);
            usedKeyList.AddFirst(node);
            nodeDic.Add(key, node);
        }
    }
}