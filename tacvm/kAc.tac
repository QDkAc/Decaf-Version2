VTABLE(_Test) {
    <empty>
    Test
    _Test.test;
    _Test.main;
}

VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_Node) {
    <empty>
    Node
    _Node.setNext;
    _Node.setId;
    _Node.count;
}

FUNCTION(_Test_New) {
memo ''
_Test_New:
    _T7 = 8
    parm _T7
    _T8 =  call _Alloc
    _T9 = VTBL <_Test>
    *(_T8 + 0) = _T9
    return _T8
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T10 = 4
    parm _T10
    _T11 =  call _Alloc
    _T12 = VTBL <_Main>
    *(_T11 + 0) = _T12
    return _T11
}

FUNCTION(_Node_New) {
memo ''
_Node_New:
    _T13 = 12
    parm _T13
    _T14 =  call _Alloc
    _T15 = VTBL <_Node>
    *(_T14 + 0) = _T15
    return _T14
}

FUNCTION(_Test.test) {
memo '_T0:4'
_Test.test:
    _T17 = 7
    _T16 = _T17
    _T18 = 0
    _T19 = (_T16 < _T18)
    if (_T19 == 0) branch _L17
    _T20 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T20
    call _PrintString
    call _Halt
_L17:
    _T21 = 4
    _T22 = (_T21 * _T16)
    _T23 = (_T21 + _T22)
    parm _T23
    _T24 =  call _Alloc
    *(_T24 + 0) = _T16
    _T25 = *(_T0 + 4)
    *(_T0 + 4) = _T24
    _T27 = 0
    _T26 = _T27
_L18:
    _T28 = (_T26 < _T16)
    if (_T28 == 0) branch _L19
    _T29 =  call _Node_New
    _T30 = *(_T0 + 4)
    _T31 = *(_T30 + 0)
    _T32 = (_T26 < _T31)
    if (_T32 == 0) branch _L20
    _T33 = 0
    _T34 = (_T26 < _T33)
    if (_T34 == 0) branch _L21
_L20:
    _T35 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T35
    call _PrintString
    call _Halt
_L21:
    _T36 = 4
    _T37 = (_T26 * _T36)
    _T38 = (_T37 + _T36)
    _T39 = *(_T30 + _T38)
    _T40 = 4
    _T41 = (_T26 * _T40)
    _T42 = (_T41 + _T40)
    *(_T30 + _T42) = _T29
    _T43 = *(_T0 + 4)
    _T44 = *(_T43 + 0)
    _T45 = (_T26 < _T44)
    if (_T45 == 0) branch _L22
    _T46 = 0
    _T47 = (_T26 < _T46)
    if (_T47 == 0) branch _L23
_L22:
    _T48 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T48
    call _PrintString
    call _Halt
_L23:
    _T49 = 4
    _T50 = (_T26 * _T49)
    _T51 = (_T50 + _T49)
    _T52 = *(_T43 + _T51)
    parm _T52
    parm _T26
    _T53 = *(_T52 + 0)
    _T54 = *(_T53 + 12)
    call _T54
    _T55 = 1
    _T56 = (_T26 + _T55)
    _T26 = _T56
    branch _L18
_L19:
    _T57 = 0
    _T26 = _T57
_L24:
    _T58 = (_T26 < _T16)
    if (_T58 == 0) branch _L25
    _T59 = *(_T0 + 4)
    _T60 = *(_T59 + 0)
    _T61 = (_T26 < _T60)
    if (_T61 == 0) branch _L26
    _T62 = 0
    _T63 = (_T26 < _T62)
    if (_T63 == 0) branch _L27
_L26:
    _T64 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T64
    call _PrintString
    call _Halt
_L27:
    _T65 = 4
    _T66 = (_T26 * _T65)
    _T67 = (_T66 + _T65)
    _T68 = *(_T59 + _T67)
    _T69 = *(_T0 + 4)
    _T70 = 2
    _T71 = (_T26 * _T70)
    _T72 = 0
    _T73 = (_T16 == _T72)
    if (_T73 == 0) branch _L28
    _T74 = "Decaf runtime error: Division by zero error."
    parm _T74
    call _PrintString
    call _Halt
_L28:
    _T75 = (_T71 % _T16)
    _T76 = *(_T69 + 0)
    _T77 = (_T75 < _T76)
    if (_T77 == 0) branch _L29
    _T78 = 0
    _T79 = (_T75 < _T78)
    if (_T79 == 0) branch _L30
_L29:
    _T80 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T80
    call _PrintString
    call _Halt
_L30:
    _T81 = 4
    _T82 = (_T75 * _T81)
    _T83 = (_T82 + _T81)
    _T84 = *(_T69 + _T83)
    parm _T68
    parm _T84
    _T85 = *(_T68 + 0)
    _T86 = *(_T85 + 8)
    call _T86
    _T87 = 1
    _T88 = (_T26 + _T87)
    _T26 = _T88
    branch _L24
_L25:
}

FUNCTION(_Test.main) {
memo '_T1:4'
_Test.main:
    _T90 = *(_T1 + 4)
    _T91 = 1
    _T92 = *(_T90 + 0)
    _T93 = (_T91 < _T92)
    if (_T93 == 0) branch _L31
    _T94 = 0
    _T95 = (_T91 < _T94)
    if (_T95 == 0) branch _L32
_L31:
    _T96 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T96
    call _PrintString
    call _Halt
_L32:
    _T97 = 4
    _T98 = (_T91 * _T97)
    _T99 = (_T98 + _T97)
    _T100 = *(_T90 + _T99)
    _T89 = _T100
    _T101 = 1
    _T102 = 0
    _T103 = (_T101 < _T102)
    if (_T103 == 0) branch _L33
    _T104 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T104
    call _PrintString
    call _Halt
_L33:
    _T105 = 4
    _T106 = (_T105 * _T101)
    _T107 = (_T105 + _T106)
    parm _T107
    _T108 =  call _Alloc
    *(_T108 + 0) = _T101
    _T109 = *(_T1 + 4)
    *(_T1 + 4) = _T108
    parm _T89
    _T110 = *(_T89 + 0)
    _T111 = *(_T110 + 16)
    _T112 =  call _T111
    parm _T112
    call _PrintInt
	call _GC
}

FUNCTION(main) {
memo ''
main:
    _T114 =  call _Test_New
    _T113 = _T114
    parm _T113
    _T115 = *(_T113 + 0)
    _T116 = *(_T115 + 8)
    call _T116
    parm _T113
    _T117 = *(_T113 + 0)
    _T118 = *(_T117 + 12)
    call _T118
}

FUNCTION(_Node.setNext) {
memo '_T2:4 _T3:8'
_Node.setNext:
    _T119 = *(_T2 + 4)
    *(_T2 + 4) = _T3
}

FUNCTION(_Node.setId) {
memo '_T4:4 _T5:8'
_Node.setId:
    _T120 = *(_T4 + 8)
    *(_T4 + 8) = _T5
}

FUNCTION(_Node.count) {
memo '_T6:4'
_Node.count:
    _T122 = *(_T6 + 4)
    _T121 = _T122
    _T124 = 1
    _T123 = _T124
_L34:
    _T125 = *(_T121 + 8)
    _T126 = *(_T6 + 8)
    _T127 = (_T125 != _T126)
    if (_T127 == 0) branch _L35
    _T128 = *(_T121 + 4)
    _T121 = _T128
    _T129 = 1
    _T130 = (_T123 + _T129)
    _T123 = _T130
    branch _L34
_L35:
    return _T123
}

