fence io,iorw
    add
    t0
    ,
    t1 ,
    t2



sub	    t3	,	t4	,	t5

fence io
sll
		t6
	,	a0
		,
		a1

ecall

srl	    a2
	    ,		a3	    ,
a4

    sra	a5
,	t0 , t1

xor		t2
	,
t3	,
t4


or	  t5
,  t6
, a0



and 	a1 ,
a2	,
a3


slt
a4
,a5,
t0
fence io,io




sltu		t1
	,
t2
	,   t3


addi		t4
,
    t5,

25

ecall


slti  	t6
, a0
	,
-13


ebreak
ecall

sltiu 		a1,
	a2, 7

xori		a3
,
	 a4
	,
42

ecall

ori		a5, t0,   	99

fence io,io
fence io,io


andi
		t1
	,	 t2,
	63



slli t3,
t4	,
4

srli		t5
,
t6,	2


srai    a0	,
a1,
1


lb 		a2
	,	 5,
a3

lh
	a4	,
-7,
a5

lw 	t0,
12,
t1


lbu
t2,
-16,
t3


lhu		t4
,	20,
t5



sb	    t6
	,	3,
a0




sh
	a1
	, -8
,
a2



sw		a3,
18
,
a4


beq		a5
,
t0
	,
16


bne
t1
,
t2, 8


blt
		t3
,
t4
,
24

bge		t5
,
t6	,
-12


bltu
a0
	,
a1
,	14


bgeu	a2,
a3
,
-20



jal
	a4,
28

jalr
	a5,
36,
t0



lui	t1,
0x5678


auipc
t2,
0x1234




mul		t3
,	t4,
t5


mulh		t6	,
	a0,
a1

mulhsu		a2,
a3,
a4

mulhu
a5,	t0,
t1

div
t2
,
t3,
t4


divu
	t5,
t6,
a0


rem
	a1, a2,
a3



remu
	a4,
a5,
t0





