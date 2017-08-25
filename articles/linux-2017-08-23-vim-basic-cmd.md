# Linux vim 基础命令
原文：http://linux.vbird.org/linux_basic/0310vi.php#vi_ex
## 三种模式

### 一般指令模式 (command mode)
    以 vi 打開一個檔案就直接進入一般指令模式了(這是預設的模式，也簡稱為一般模式)。在這個模式中， 你可以使用『上下左右』按鍵來移動游標，你可以使用『刪除字元』或『刪除整列』來處理檔案內容， 也可以使用『複製、貼上』來處理你的文件資料。

### 編輯模式 (insert mode)
    在一般指令模式中可以進行刪除、複製、貼上等等的動作，但是卻無法編輯文件內容的！ 要等到你按下『i, I, o, O, a, A, r, R』等任何一個字母之後才會進入編輯模式。注意了！通常在 Linux 中，按下這些按鍵時，在畫面的左下方會出現『 INSERT 或 REPLACE 』的字樣，此時才可以進行編輯。而如果要回到一般指令模式時， 則必須要按下『Esc』這個按鍵即可退出編輯模式。

### 指令列命令模式 (command-line mode)
    在一般模式當中，輸入『 : / ? 』三個中的任何一個按鈕，就可以將游標移動到最底下那一列。在這個模式當中， 可以提供你『搜尋資料』的動作，而讀取、存檔、大量取代字元、離開 vi 、顯示行號等等的動作則是在此模式中達成的！
    

## 按鍵說明
第一部份：一般指令模式可用的按鈕說明，游標移動、複製貼上、搜尋取代等
### 移动光标的方法

```bash
h 或 向左方向鍵(←)	游標向左移動一個字元
j 或 向下方向鍵(↓)	游標向下移動一個字元
k 或 向上方向鍵(↑)	游標向上移動一個字元
l 或 向右方向鍵(→)	游標向右移動一個字元

# 如果你將右手放在鍵盤上的話，你會發現 hjkl 是排列在一起的，因此可以使用這四個按鈕來移動游標。 如果想要進行多次移動的話，例如向下移動 30 列，可以使用 "30j" 或 "30↓" 的組合按鍵， 亦即加上想要進行的次數(數字)後，按下動作即可！

[Ctrl] + [f]	    螢幕『向下』移動一頁，相當於 [Page Down]按鍵 (常用)
[Ctrl] + [b]	    螢幕『向上』移動一頁，相當於 [Page Up] 按鍵 (常用)
[Ctrl] + [d]	    螢幕『向下』移動半頁
[Ctrl] + [u]	    螢幕『向上』移動半頁
+	                游標移動到非空白字元的下一列
-	                游標移動到非空白字元的上一列
n<space>	        那個 n 表示『數字』，例如 20 。按下數字後再按空白鍵，游標會向右移動這一列的 n 個字元。例如 20<space> 則游標會向後面移動 20 個字元距離。
0 或功能鍵[Home]	    這是數字『 0 』：移動到這一列的最前面字元處 (常用)
$ 或功能鍵[End]	    移動到這一列的最後面字元處(常用)
H	                游標移動到這個螢幕的最上方那一列的第一個字元
M	                游標移動到這個螢幕的中央那一列的第一個字元
L	                游標移動到這個螢幕的最下方那一列的第一個字元
G	                移動到這個檔案的最後一列(常用)
nG	                n 為數字。移動到這個檔案的第 n 列。例如 20G 則會移動到這個檔案的第 20 列(可配合 :set nu)
gg	                移動到這個檔案的第一列，相當於 1G 啊！ (常用)
n<Enter>	        n 為數字。游標向下移動 n 列(常用)
```

### 查找与替换

```bash
/word	向游標之下尋找一個名稱為 word 的字串。例如要在檔案內搜尋 vbird 這個字串，就輸入 /vbird 即可！ (常用)
?word	向游標之上尋找一個字串名稱為 word 的字串。
n	    這個 n 是英文按鍵。代表『重複前一個搜尋的動作』。舉例來說， 如果剛剛我們執行 /vbird 去向下搜尋 vbird 這個字串，則按下 n 後，會向下繼續搜尋下一個名稱為 vbird 的字串。如果是執行 ?vbird 的話，那麼按下 n 則會向上繼續搜尋名稱為 vbird 的字串！
N	    這個 N 是英文按鍵。與 n 剛好相反，為『反向』進行前一個搜尋動作。 例如 /vbird 後，按下 N 則表示『向上』搜尋 vbird 。

#使用 /word 配合 n 及 N 是非常有幫助的！可以讓你重複的找到一些你搜尋的關鍵字！

:n1,n2s/word1/word2/g	n1 與 n2 為數字。在第 n1 與 n2 列之間尋找 word1 這個字串，並將該字串取代為 word2 ！舉例來說，在 100 到 200 列之間搜尋 vbird 並取代為 VBIRD 則：『:100,200s/vbird/VBIRD/g』。(常用)
:1,$s/word1/word2/g	    從第一列到最後一列尋找 word1 字串，並將該字串取代為 word2 ！(常用)
:1,$s/word1/word2/gc	從第一列到最後一列尋找 word1 字串，並將該字串取代為 word2 ！且在取代前顯示提示字元給使用者確認 (confirm) 是否需要取代！(常用)
```

### 删除、复制和黏贴

```bash
x, X	在一列字當中，x 為向後刪除一個字元 (相當於 [del] 按鍵)， X 為向前刪除一個字元(相當於 [backspace] 亦即是倒退鍵) (常用)
nx	    n 為數字，連續向後刪除 n 個字元。舉例來說，我要連續刪除 10 個字元， 『10x』。
dd	    刪除游標所在的那一整列(常用)
ndd	    n 為數字。刪除游標所在的向下 n 列，例如 20dd 則是刪除 20 列 (常用)
d1G	    刪除游標所在到第一列的所有資料
dG	    刪除游標所在到最後一列的所有資料
d$	    刪除游標所在處，到該列的最後一個字元
d0	    那個是數字的 0 ，刪除游標所在處，到該列的最前面一個字元
yy	    複製游標所在的那一列(常用)
nyy	    n 為數字。複製游標所在的向下 n 列，例如 20yy 則是複製 20 列(常用)
y1G	    複製游標所在列到第一列的所有資料
yG	    複製游標所在列到最後一列的所有資料
y0	    複製游標所在的那個字元到該列行首的所有資料
y$	    複製游標所在的那個字元到該列行尾的所有資料
p, P    	p 為將已複製的資料在游標下一列貼上，P 則為貼在游標上一列！ 舉例來說，我目前游標在第 20 列，且已經複製了 10 列資料。則按下 p 後， 那 10 列資料會貼在原本的 20 列之後，亦即由 21 列開始貼。但如果是按下 P 呢？ 那麼原本的第 20 列會被推到變成 30 列。 (常用)
J	    將游標所在列與下一列的資料結合成同一列
c	    重複刪除多個資料，例如向下刪除 10 列，[ 10cj ]
u	    復原前一個動作。(常用)
[Ctrl]+r	重做上一個動作。(常用)

# 這個 u 與 [Ctrl]+r 是很常用的指令！一個是復原，另一個則是重做一次～ 利用這兩個功能按鍵，你的編輯，嘿嘿！很快樂的啦！

.	    不要懷疑！這就是小數點！意思是重複前一個動作的意思。 如果你想要重複刪除、重複貼上等等動作，按下小數點『.』就好了！ (常用)
```

第二部份：一般指令模式切換到編輯模式的可用的按鈕說明

### 进入插入或替换的编辑模式

```bash
i, I	進入插入模式(Insert mode)：
i       為『從目前游標所在處插入』， I 為『在目前所在列的第一個非空白字元處開始插入』。 (常用)
a, A	進入插入模式(Insert mode)：
a       為『從目前游標所在的下一個字元處開始插入』， A 為『從游標所在列的最後一個字元處開始插入』。(常用)
o, O	進入插入模式(Insert mode)：

# 這是英文字母 o 的大小寫。o 為『在目前游標所在的下一列處插入新的一列』； O 為在目前游標所在處的上一列插入新的一列！(常用)

r, R	進入取代模式(Replace mode)：
r       只會取代游標所在的那一個字元一次；R會一直取代游標所在的文字，直到按下 ESC 為止；(常用)

# 上面這些按鍵中，在 vi 畫面的左下角處會出現『--INSERT--』或『--REPLACE--』的字樣。 由名稱就知道該動作了吧！！特別注意的是，我們上面也提過了，你想要在檔案裡面輸入字元時， 一定要在左下角處看到 INSERT 或 REPLACE 才能輸入喔！

[Esc]	退出編輯模式，回到一般指令模式中(常用)
```

第三部份：一般指令模式切換到指令列模式的可用按钮说明

### 指令列模式的保存、离开等指令

```bash
:w	                將編輯的資料寫入硬碟檔案中(常用)
:w!	                若檔案屬性為『唯讀』時，強制寫入該檔案。不過，到底能不能寫入， 還是跟你對該檔案的檔案權限有關啊！
:q	                離開 vi (常用)
:q!	                若曾修改過檔案，又不想儲存，使用 ! 為強制離開不儲存檔案。
    
# 注意一下啊，那個驚嘆號 (!) 在 vi 當中，常常具有『強制』的意思～
    
:wq	                儲存後離開           ，若為 :wq! 則為強制儲存後離開 (常用)
ZZ	                這是大寫的 Z 喔！若檔案沒有更動，則不儲存離開，若檔案已經被更動過，則儲存後離開！
:w [filename]	    將編輯的資料儲存成另一個檔案（類似另存新檔）
:r [filename]	    在編輯的資料中，讀入另一個檔案的資料。亦即將 『filename』 這個檔案內容加到游標所在列後面
:n1,n2 w [filename]	將 n1 到 n2 的內容儲存成 filename 這個檔案。
:! command	        暫時離開 vi 到指令列模式下執行 command 的顯示結果！例如『:! ls /home』即可在 vi 當中察看 /home 底下以 ls 輸出的檔案資訊！
```

### vim 环境的变更

```bash
:set nu	    顯示行號，設定之後，會在每一列的字首顯示該列的行號
:set nonu	與 set nu 相反，為取消行號！
```