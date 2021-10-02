# Atcoder diary


___ 

training1 ~

time : 1hours

Exclude experimental difficulty

difficulty
1. 800~1200
2. 800~1200
3. 1200~1600

___
### 2021/09/20  
- training1  
    1. [D - Flipping Signs](https://atcoder.jp/contests/abc125/tasks/abc125_d)  
    配列にある正、負、零の数に着目するらしい。  
    例えば負の数が偶数の場合はすべて正の数に変えることができる。  
    場合分けと貪欲法を使った問題
    2. [C - 755](https://atcoder.jp/contests/abc114/tasks/abc114_c)  
    再帰関数を書いて全探索、高々3^9t程度  
    flag管理にbitを使って簡略化した
    3. [D - Patisserie ABC](https://atcoder.jp/contests/abc100/tasks/abc100_d)  
    x,y,zの配列に対し、それぞれの絶対値の和の最大値を求めたい。  
    このときある配列に対して最も大きい和か最も小さい和を求めたらよい  
    これはそれぞれの配列全体にそのままか-1かけるかの2^3通りで探索できる


___
### 2021/09/21  
- training2  
    1. [A - Biscuits](https://atcoder.jp/contests/agc017/tasks/agc017_a)  
    パリティに着目する問題
    2. [C - 次のアルファベット](https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_c)  
    少し複雑だが実装するだけ  
    3. [E - Colorful Blocks](https://atcoder.jp/contests/abc167/tasks/abc167_e)  


___ 

training4 ~

time : 1hours

Exclude experimental difficulty

difficulty
1. 800~1200
2. 1200~1600


___

### 2021/09/30
- training4(1,2)
    1. [E - This Message Will Self-Destruct in 5s](https://atcoder.jp/contests/abc166/tasks/abc166_e)  
    Ai+Aj = j-i となるペアを数え上げる  
    この状態ではiとjは独立してないため計算量を落とし込めない  
    そこで Ai+i = j-Aj と式変形することでそれぞれが独立した式にできる  
    後はそれぞれ(2つ)の配列を用意し同じ値となるものがいくつあるか数える
    2. [D - Decayed Bridges ](https://atcoder.jp/contests/abc120/tasks/abc120_d)  
    **連結成分を分けることは難しい**  
    これを実装しようとしてうまくいかず時間切れ...  
    今回**連結を分離させていく操作は、時間を逆に見て連結させていく操作で考える**というテクを使う  
    つまり連結によって不便さがどれだけ減るかを考える  
    また不便さは最初は(N-1)*N//2であり、  
    サイズがa,bのグループが連結すると不便さがa*b分減る


- training5(1)
    1. [C - Back and Forth](https://atcoder.jp/contests/abc051/tasks/abc051_c)  
    bfsで通った道を保持しながら探索するものだと思った  
    だがこの時問題となったのがrouteの保持方法である  
    これが思いつかず時間切れ  
    解法を見るとこの問題では難しいアルゴリズムを考える必要がなく、  
    1回目と2回目で1周り分ずらすと答えとなる  
    常にsx,syが左下でtx,tyが右上にあるという点を意識してたら  
    この問題の本質に気づけた
    2. [D - Even Relation](https://atcoder.jp/contests/abc126/tasks/abc126_d)  
    dfsで長さを保持しながら探索  
    水difの難易度ではない


___
### 2021/10/01
- training6(2)
    1. [D - Enough Array](https://atcoder.jp/contests/abc130/tasks/abc130_d)  
    しゃくとり法  
    右端を全探索して左端を右端に近づけていく  
    解説では左端を全探索して右端をK未満である限り伸ばしていた。  
    こちらのほうがイメージしやすい
    2. [E - All-you-can-eat](https://atcoder.jp/contests/abc145/tasks/abc145_e)  
    動的計画法  
    dp[i][j]:=i個目までの料理でj分以下で作れるものの満足度の最大値  
    ただし、時間制限に関係なく最後に一つ料理を食べられるのが  
    この問題のキーポイントである  
    そこでT分未満で作れる料理の最大値を求め最後に満足度を足して  
    ansを更新していく


- training7(1,2)
    1. [C - Factors of Factorial](https://atcoder.jp/contests/arc067/tasks/arc067_a)  
    1からNについて素因数分解して  
    その素因数の数に１足したものをmodで割りながらかけていく
    2. [E - Third Avenue](https://atcoder.jp/contests/abc184/tasks/abc184_e)  
    幅優先探索  
    テレポート先をあらかじめ記録しておき、初めてそのテレポーターへ来たとき  
    ほかのテレポーターへワープして探索する  
    そうでない場合通常の探索をする  
    あと、pypy3では通ったがpythonではTLEなので注意




___
### 2021/10/02
- training8
    1. [C - Exoswap](https://atcoder.jp/contests/arc110/tasks/arc110_c)  
    ミスのない実装が必要  
    考察自体は単純で例えば1がどの場所にあろうと最終的に  
    一番右に来る必要があるので貪欲に入れ替えていけばよい  
    その際にi,i-1間の入れ替えを行ったかを保持しておく  
    すでに入れ替えが行われていた場合はexit
    2. []()  
    見る時間がなかったので略
