#define MIN_VAL(x, y)   ((x) < (y) ? (x) : (y))

/* 链表。在生成邻接点列表时使用。 */
typedef struct
{
    int node;
    int next;
}
LinkedNode;

/* 双端队列。在广度优先搜索时使用。 */
typedef struct
{
    int *arr;
    int arrHead;
    int arrSize;
    int totalLength;
}
BinodeQueue;

/* 队列的push、pop操作。 */
static void queuePush(BinodeQueue *queue, int node);
static void queuePop(BinodeQueue *queue);

/* 几个局部变量的说明。
  neighbourSize:        edges数组中，两个端点互为对方的邻居，所以需要的链表节点数是其两倍。
  x, y, z:              循环变量。
  result:               要求的结果。按照题意，如果图中没有环，返回-1，故初始化为-1。
  arr[n]:               队列使用的数组空间。
  heads[n]:             链表的头节点下标。每个节点的邻接点列表，在这里以链表形式存在。初始化为无效下标-1。
  distance[n]:          枚举每一条可能删除的边时，从其中一端出发，其它所有节点的最近距离。
  queue:                双端队列。在广度优先搜索时使用。
  buff:                 各个邻接点列表所需要的所有链表节点的空间，存在一个长度neighbourSize的数组中。 */
int findShortestCycle(int n, int **edges, int edgesSize, int *edgesColSize)
{
    const int neighbourSize = edgesSize << 1;
    int x = 0, y = 0, z = 0, result = -1;
    int arr[n], heads[n], distance[n];
    BinodeQueue queue;
    LinkedNode buff[neighbourSize];
    /* 初始化双端队列，以及各个节点的邻居链表。 */
    queue.arr = arr;
    queue.arrHead = 0;
    queue.arrSize = 0;
    queue.totalLength = n;
    memset(heads, -1, sizeof(heads));
    /* 生成各个节点的邻居链表。 */
    for(x = 0; edgesSize > x; x++)
    {
        /* edges[x][1]是edges[x][0]的邻居。 */
        buff[z].node = edges[x][1];
        buff[z].next = heads[edges[x][0]];
        heads[edges[x][0]] = z;
        z++;
        /* edges[x][0]是edges[x][1]的邻居。 */
        buff[z].node = edges[x][0];
        buff[z].next = heads[edges[x][1]];
        heads[edges[x][1]] = z;
        z++;
    }
    /* 遍历每一条可能被删除的边。 */
    for(x = 0; edgesSize > x; x++)
    {
        /* 当删除edges[x]这条边之后，查看edges[x][0]到edges[x][1]的最短距离。
        先初始化队列、距离数组，以及，把起点先加到队列中。 */
        queue.arrSize = 0;
        memset(distance, -1, sizeof(distance));
        distance[edges[x][0]] = 0;
        queuePush(&queue, edges[x][0]);
        /* 然后逐个进行邻居扩散。 */
        while(0 < queue.arrSize && -1 == distance[edges[x][1]])
        {
            /* 队首节点出队的同时，把邻居们入队。 */
            y = queue.arr[queue.arrHead];
            queuePop(&queue);
            /* 只需要把还未曾加入过队列的节点入队，注意要避开被删除的边。 */
            for(z = heads[y]; -1 != z; z = buff[z].next)
            {
                if(-1 == distance[buff[z].node]
                    && (y != edges[x][0] || buff[z].node != edges[x][1])
                    && (y != edges[x][1] || buff[z].node != edges[x][0]))
                {
                    distance[buff[z].node] = distance[y] + 1;
                    queuePush(&queue, buff[z].node);
                }
            }
        }
        /* 最终如果能到达edges[x][1]，则更新最短距离。注意result是初始化为-1的。 */
        if(-1 != distance[edges[x][1]])
        {
            result = (-1 == result) ? distance[edges[x][1]] + 1 : MIN_VAL(result, distance[edges[x][1]] + 1);
        }
    }
    return result;
}

/* 双端队列，push时将元素放到队尾。注意这里的队列是环形数组，数组往右越界时回到数组头部。 */
static void queuePush(BinodeQueue *queue, int node)
{
    int x = (queue->totalLength > queue->arrHead + queue->arrSize) ? queue->arrHead + queue->arrSize : queue->arrHead + queue->arrSize - queue->totalLength;
    queue->arr[x] = node;
    queue->arrSize++;
    return;
}

/* 双端队列，pop时从队首弹出。注意这里的队列是环形数组，数组往右越界时回到数组头部。 */
static void queuePop(BinodeQueue *queue)
{
    queue->arrHead = (queue->totalLength - 1 == queue->arrHead) ? 0 : queue->arrHead + 1;
    queue->arrSize--;
    return;
}