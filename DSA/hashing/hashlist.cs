
class Program
{
    static void Main()
    {
        int[] varArray = new int[5]; // equivalent to var = [0]*5
        int n = 10_000_000;

        List<int> newList = new List<int>(n); // dynamic array with preallocated capacity
        for (int i = 0; i < n; i++)
        {
            newList.Add(i);
        }

        Console.WriteLine(newList[newList.Count - 1]); // equivalent to new[-1]
    }
}
