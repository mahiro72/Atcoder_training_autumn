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

training3 ~

time : 1hours

Exclude experimental difficulty

difficulty
1. 800~1200
2. 1200~1600


___

### 2021/09/27  
- training3  
    1. [B - Palindrome-phobia](https://atcoder.jp/contests/cf17-final/tasks/cf17_final_b)  
    現在は回文か、また入れ替えると回文になるかなどに着目してはいけない  
    与えられたSで回文ではない文字を作れるかどうかがキーである  
    今回はa,b,cの3文字しか使われないため、abcabc...となる必要がある。
    2. [E - Roaming](https://atcoder.jp/contests/abc156/tasks/abc156_e)  
    重複組み合わせ  
    よくわからなかった。。。