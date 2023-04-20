        public class NestedIterator
        {
            private Queue<int> q = new Queue<int>();

            public NestedIterator(IList<NestedInteger> nestedList)
            {
                foreach (var item in nestedList)
                    DFS(item);
            }

            public bool HasNext()
            {
                return q.Count != 0;
            }

            public int Next()
            {
                return q.Count == 0 ? 0 : q.Dequeue();
            }

            private void DFS(NestedInteger cur)
            {
                if (cur.IsInteger())
                    q.Enqueue(cur.GetInteger());
                else
                    foreach (var item in cur.GetList())
                        DFS(item);
            }
        }