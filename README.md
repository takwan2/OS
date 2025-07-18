# 環境構築
こちらのURLを参考にしてください。

参考: [mikanos-build](https://github.com/uchan-nos/mikanos-build)


# 用語解説
自作OSに欠かせない用語の解説をします。

## OS

### OSとは何か？

OS（オペレーティングシステム）とは何かを一言で定義するのは実は難しいものです。

たとえば『30日でできる！OS自作入門』では、次のように述べられています。

>実は人によって何を OS と呼ぶかはばらつきがあり、バシっと定義することは難しそうです。「さまざまなOSを比較してみたところ、この機能が共通点、といえそうなものを見つけられませんでした。結局のところ、それぞれの作者が『これは OS なんだ』と言い張って、周囲の人も『まあそうかな』と思えばどんなソフトでも OS なんです」。

確かに、シンプルな機能しか持たないにもかかわらず「OS」と呼ばれるソフトウェアも多く存在します。そのため、「すべてのOSに共通する機能」を見つけるのは非常に困難です。


### OSを構成する3つの側面
そんな中でも、Windows・macOS・Linux などの代表的なOSに共通する特徴を見てみると、OSには大きく次の3つの側面があることがわかります。

1. アプリケーションに対するインターフェースとしての側面
2. 計算資源分配者としての側面
3. 人間に対するインターフェースとしての側面

### 1. アプリケーションに対するインターフェースとしての側面
OSは、アプリケーションとハードウェアの間に立つ「インターフェース」の役割を果たします。

例えば、メモ帳アプリでファイルを保存するとき、アプリ側は次のような関数を呼び出すだけで済みます

```
fopen("data.txt");  // ファイルを開く  
fwrite();           // 書き込む  
fclose();           // 閉じる  
```

どのストレージ（HDD、SSD、USBなど）に、どのフォーマット形式（FAT32、ext4など）で保存するかはOSが抽象化して扱ってくれるため、アプリはそれを意識する必要がありません。

このように、異なる周辺機器であっても同じ関数で扱えるのは、OSが統一されたインターフェースを提供しているからです。

### 2. 計算資源の分配者
OSはCPUやメモリといった限られた資源を、複数のアプリケーションの間でうまく配分する役割も担います。

たとえば、動画エンコードのようにCPUを大量に消費する処理を行っているとき、同時にマウスを動かすとします。
もしOSが動画エンコードにCPUを100%使わせてしまうと、マウスの動きが止まってしまい、まるでフリーズしたように見えてしまいます。

OSは、こうした処理の緊急度や特性を考慮して、CPUの使い方を調整します。
マウスのように即時応答が求められる処理には素早く対応しつつ、動画エンコードのように多少遅れてもよい処理は後回しにすることで、システム全体の快適さを保ちます。

### 3. 人間に対するインターフェース
OSは、人間がコンピュータを操作するための共通のインターフェースも提供しています。

たとえば、どんなアプリケーションでも画面右上には「×」ボタンがあり、ファイルメニューには「名前を付けて保存」や「上書き保存」があります。
これは、OSが統一されたユーザーインターフェースを提供しているおかげです。

OSは「人とアプリケーションの間」を仲介する役割も担っており、ユーザーが直感的にコンピュータを操作できるように設計されています。

### インターフェースとは？
ここで言う「インターフェース」とは、「2つのものが接する場所・手段」のことです。いくつかの例を挙げると：

人間と炊飯器
→ インターフェースは「ボタン」
（たとえば「早炊き」ボタンを押すと、自動で調整されてご飯が炊ける）

患者と病院
→ インターフェースは「受付」
（ 「腰が痛い」と伝えれば、受付が整形外科を案内してくれる）

OSも、アプリとハードウェア、人間とアプリの間に立つ「インターフェース」として機能しているのです。

## BIOS
### BIOSとは
BIOS（Basic Input/Output System）は、コンピュータ本体にあらかじめ内蔵されているプログラムです。
OSやアプリとは異なり、BIOSはROMに記録されており、電源を切っても消えません。

BIOSは、コンピュータの電源投入直後に最初に実行される「ファームウェア」と呼ばれるプログラムで、主に以下の役割を担います：

- コンピュータ内部の初期化（CPU設定、デバイス検出など）

- ストレージからブートローダーを読み込み、OSの起動につなげる

#### フラッシュROMによるアップデート
最近のBIOSは、書き換え可能なフラッシュROMに記録されていることが多く、以下のようなことが可能です：

- ファームウェアの不具合修正

- 機能追加や拡張

- セキュリティ更新

たとえば、Web経由でファームウェアを配布・更新する仕組みが導入されています。これにより、現場で稼働中の機器にも柔軟にアップデートを適用できます。

## UEFI
### UEFIとは？
UEFI（Unified Extensible Firmware Interface）は、ファームウェアとOSの間をつなぐインターフェース仕様です。
重要なのは、UEFIが「仕様」であるという点であり、特定のプロセッサアーキテクチャ（Intel, AMD, ARM など）に依存しません。

### 「UEFI BIOS」と呼ばれる理由
UEFIの機能を備えたファームウェアは、「UEFI BIOS」や単に「UEFI」と呼ばれることがあります。
ただし、PC/AT互換機のアーキテクチャでは、ユーザーが設定を行うGUI画面などを含めて、従来どおり「BIOS」と呼ばれることも多くあります。

## 電源投入後のBIOSの処理の流れ
コンピュータの電源が投入されてから、OSが起動されるまでの流れは以下のようになります：

1. CPUがBIOSを実行開始

2. BIOSが初期化処理を実行

- 例：CPU動作モードの設定

- デバイスの検出（メモリ、キーボード、ストレージなど）

3. ストレージ上の実行可能ファイル（ブートローダ）を検索

4. ブートローダをメインメモリに読み込み

5. BIOSが処理をCPUに引き渡し、ブートローダが実行される



## システムコール（System Call）

### システムコールとは？
システムコールとは、アプリケーションがOSの機能を利用するための呼び出し手段のことです。
OSが提供するハードウェア制御の機能は、一般的に多数の小さな関数として実装されており、これらを「システムコール」と呼びます。

たとえば、以下のような関数も内部的にはシステムコールを利用しています：

```
fopen();   // ファイルを開く  
printf();  // 標準出力に文字列を表示する  
```

### システムコールを直接使わない理由
C言語などの高水準言語は、OSに依存しないソースコードを書くことを目的としています。
同じソースコードが Windows でも Linux でも動作するのは、以下のような仕組みがあるためです：

- 高水準言語で記述された関数（例：fopen）が、コンパイル時にそのOSに対応したシステムコールに変換される

一部のプログラミング言語やライブラリでは、システムコールを直接呼び出すことも可能ですが、その場合はOSに強く依存するコードとなるため、移植性が損なわれます。

例：Windowsのシステムコールを直接呼ぶアプリケーションは、Linuxでは動作しません。


## 実行可能ファイルの種類
### スクリプトと機械語プログラムの違い
スクリプト
スクリプトは、人間が読めるコードで書かれており、**インタプリタ（解釈器）**によって実行されます。
代表的なスクリプト言語：

- シェルスクリプト（.sh）
- Python（.py）

### 機械語プログラム
機械語プログラムは、CPUが直接実行できるバイナリ形式の命令で構成されています。
この種のファイルは、あらかじめコンパイルとリンクを行って作成されます。

| OS | 実行形式 | 拡張子 |
|:-----------|----------:|:------------:|
| Windows    |   PE形式  |     .exe     |
| Linux      |   ELF形式 |    なし（実行権限があればOK）    |


### オブジェクトファイルと実行可能形式

#### COFF形式とPE形式（Windows）
**COFF（Common Object File Format）**は、中間生成物である「オブジェクトファイル」に使われる形式です。

Windowsでは、COFF形式のファイルをリンクして**PE形式（Portable Executable）**の実行ファイル（.exe）を生成します。

#### ELF形式（Linux）
ELF（Executable and Linkable Format）は、その名の通り、実行可能ファイルとリンク可能なオブジェクトファイルの両方を表現できる形式です。

Linuxでは標準的にこの形式が用いられており、コンパイルから実行まで一貫して扱えます。

#### ファイル形式の比較と例え
PE、COFF、ELFはいずれも、x86-64 CPU向けの機械語を格納するファイル形式です。
この関係性は、以下のように例えることができます：

> Word / PDF / HTML の違い
→ いずれも「文章」を表現できるが、内部の構造やメタ情報の持ち方が異なる

同様に、

PE形式：Windowsの実行可能ファイル（主に.exe）

COFF形式：Windowsの中間生成ファイル（オブジェクトファイル）

ELF形式：Linuxの汎用的なバイナリ形式（実行ファイル・オブジェクトファイル両方に対応）

実行可能ファイル形式の主流
現在広く使われている実行可能ファイル形式は以下の2つです：

- PE形式（Windows）
- ELF形式（Linux）

どちらもプラットフォームごとに最適化されており、それぞれのOSで標準的に採用されています。


## ABI（Application Binary Interface）

### ABIとは？

**ABI（Application Binary Interface）** は、**プログラムとCPUの間の取り決め**を機械語レベルで定義する仕様です。

- レジスタやメモリの使い方を規定する
- コンパイラはABIに従って機械語を生成する
- OSの内部もこのABIを考慮して設計される必要がある

---

### 代表的なABI（x86-64）

x86-64アーキテクチャにおいて、以下の2種類のABIが広く使われています：

| ABI名               | 使用されるプラットフォーム |
|---------------------|----------------------------|
| System V AMD64 ABI  | Linux                      |
| Microsoft x64 ABI   | Windows                    |

> これら2つのABIは**互換性がなく**、関数呼び出しの方法などが異なります。

---

### 呼び出し規約（Calling Convention）

ABIの中でも特に重要なのが、**関数の呼び出し方法に関する規約（Calling Convention）**です。

呼び出し規約では次のようなことが定められます：

- **引数をどのレジスタで渡すか**
- **戻り値をどのレジスタで返すか**
- **関数内で変更してよいレジスタはどれか**

---

### System V AMD64 ABI の呼び出し規約（Linux）

#### 引数の渡し方

64ビットまでの整数やポインタ型の引数は、次の順序でレジスタに割り当てられます：

> RDI → RSI → RDX → RCX → R8 → R9


### 戻り値の返し方

- 戻り値は `RAX` を使って返されます
- 複数の戻り値がある場合には `RDX` も使用されます

例（1つの整数を返す）：

```asm
mov rax, 42   ; 戻り値をRAXに設定
ret           ; 呼び出し元に制御を戻す
```

## CPU（Central Processing Unit）

- メモリにロードされた**マシン語の命令**を、順に読み込んで**解釈・実行**することで、情報の加工や処理を行う。
- 通常は **バス（信号線）** を介して以下の装置と接続されている：
  - **主記憶装置（RAM）**
  - **入出力回路（I/O）**
- 入出力回路の先には、以下のような**周辺機器**が接続される：
  - 補助記憶装置（HDD、SSDなど）
  - 通信装置（ネットワークインタフェースなど）

こうして、CPUは**データやプログラムとのやりとり**を実現している。

---

## ブートローダ（Bootloader）

- ブートローダは、**OSをメインメモリに読み込み、起動させるためのプログラム**です。
- BIOSやUEFIによって呼び出され、OSのカーネルをメモリ上に配置し、制御を移します。

ブートローダがなければ、OSは起動しません。

---

## コンパイル（Compile）

- **コンパイルとは**、高水準言語（C言語など）で書かれたプログラムを、CPUが理解できる**マシン語に変換**する作業です。
- この変換を行うプログラムのことを **コンパイラ（Compiler）** と呼びます。

```text
C言語（高水準） → コンパイル → マシン語（バイナリ）
```

## メモリマップ（Memory Map）

### メモリマップとは？

**メモリマップ**とは、あるアドレス空間の中で「どのアドレスがどの用途・デバイス・機能に対応しているか」を示す**地図のようなもの**です。

大きく分けて、以下の3種類に分類されます：

1. OSやBIOSが提供する「メインメモリ領域のメモリマップ」
2. メモリマップドI/O（MMIO）
3. 組み込み機器のメモリマップ

---

### 1. メインメモリ領域のメモリマップ（OS/BIOS提供）

- **OSが安全に動作するために不可欠な情報**
- 使用可能なメモリ領域を正しく把握する必要がある
- 例：CPUの設定情報が書かれたメモリ領域を誤って上書きしてしまうと、CPUが誤作動を起こす可能性がある

> ブート時にBIOSやUEFIが提供することが多い

---

### 2. メモリマップドI/O（MMIO）

- CPUの**メモリアドレス空間**に、**デバイス**が直接割り当てられている方式
- **I/Oポートを経由せずに、メモリ空間を介して周辺機器と通信**する

#### 例：

| アドレス範囲       | 用途                     |
|-------------------|--------------------------|
| `0xFE000000〜`    | ビデオカードのVRAM       |
| `0xFEC00000`      | APIC（割り込みコントローラ） |

---

### 3. 組み込み機器のメモリマップ

- 主にマイコン（マイクロコントローラ）で使われる
- **Flash、RAM、I/Oレジスタ**などが明確にアドレスにマッピングされている

> ハードウェアに密接に関連する設計であり、**データシートやマニュアルに記載**されていることが多い

## レジスタとは

**レジスタ**は、CPUに内蔵された**高速な記憶領域**です。

- 通常、**汎用レジスタ**と**特殊レジスタ**の2種類が搭載されています。
- CPUのアーキテクチャによって、
  - レジスタの**数**
  - **種類**
  - **格納できる値のサイズ（ビット幅）**
  は異なります。

---

### 汎用レジスタ（General Purpose Register）

- **演算やデータの一時保存**など、汎用的に使用される
- メインメモリと同様に「値を記憶する」役割があるが、
  - **アクセス速度が非常に速い**
  - **CPUの中に直接組み込まれている**ため、処理効率が良い

---

### 特殊レジスタ（Special Purpose Register）

- CPUの**制御や設定に関する情報を保持**
- 例：
  - **プログラムカウンタ（PC）**：次に実行する命令のアドレス
  - **スタックポインタ（SP）**：スタックの先頭を指す
  - **フラグレジスタ（Flags）**：演算結果に基づく状態フラグ
  - **タイマや割り込み制御**に使われるレジスタ

---

## バスとは？

**バス（Bus）**は、コンピュータ内部および外部の各回路が**データを交換するための共通の経路**を指します。

- 名称の由来は、**乗り物のバス**と同じ
- 複数の装置が「相乗り」して通信を行う仕組み
  - 一対一での専用接続ではなく、共通の線に複数の機器が接続される

---

### バスの例と分類

| バスの種類     | 用途例                               |
|----------------|----------------------------------------|
| データバス     | 実際のデータをやりとりする             |
| アドレスバス   | メモリアドレスを指定する               |
| コントロールバス | 読み書き制御や割り込みなどの信号伝達     |
