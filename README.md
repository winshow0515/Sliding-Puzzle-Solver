# Sliding-Puzzle-Solver
a fast Sliding Puzzle solver!

## Prerequisite
Python 3.13.1

## generator.py
* `generate_puzzle()`
    隨機將0~5的數字填入board，效果如下圖

![image](Images/upload_7f21dfecd34c84120d4119dc617d05ea.png)

![image](Images/upload_11b36fc704f1ca14f87924b7f715a0b5.png)

### 使用方法

先創建一個名為testcases的空資料夾，在終端執行generator.py即可生成測資

可更改第10行的random.seed()裡的數字產生不同的隨機測資
```python
random.seed(3686) #-> random.seed(1)
```


## Solver.py
* `getPossibilities(self, board, x, y)` 

    回傳board下一步可能的狀態

* `slidingPuzzle(self, board: List[List[int]])` 

    用 DFS回溯法搭配 `getPossibilities()` 來嘗試完成puzzle，若有解則回傳完成需要的步數，若無解則回傳-1

``` python
from src.solver import Solution
solution = Solution()
solution.slidingPuzzle(board)
...
```
## util.py
* `read_board(path)`

    讀取測資檔的函式

## judge.py
讀入testcases資料夾裡的測資，並呼叫 `slidingPuzzle()` 完成數獨，輸出每個測資的完成時間如以下的 Testing

## Testing
|      testcases       |    time     |
|  ------------------  | ----------- |
|    testcases/0.in    |  0.007566   |
|    testcases/1.in    |  0.006899   |
|    testcases/2.in    |  0.011454   |
|    testcases/3.in    |  0.003669   |
|    testcases/4.in    |  0.003927   |
|    testcases/5.in    |  0.000725   |
|    testcases/6.in    |  0.013301   |
|    testcases/7.in    |  0.002436   |
|    testcases/8.in    |  0.004705   |
|    testcases/9.in    |  0.005822   |

## 小心得
這是我第一次自己寫專案，專案功能不算難，但實作過程練習了很多專案開發的基本技能，例如寫README.md文件、使用git和GitHub等，收穫頗豐。