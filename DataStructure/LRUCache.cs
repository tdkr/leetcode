using System.Collection.Generic;

public class LRUCache {
	int latestUsedKey;

	int capacity = 0;
	Dictionary<int, int> map = new Dictionary<int,int>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }

    public int Get(int key) {
    	latestUsedKey = key;

        if(map.Contains(key) return map[key]);
        return -1;
    }

    public void Set(int key, int value) {     
    	if(map.Count < capacity)
    	{   
        if(map.Contains(key) 
        	map[key] = value;
        else
        	map.Add(key, value);
        }
        else {
        	
        	
        }
    }
}