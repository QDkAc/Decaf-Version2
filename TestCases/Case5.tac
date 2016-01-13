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

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T5 = 4
    parm _T5
    _T6 =  call _Alloc
    _T7 = VTBL <_Main>
    *(_T6 + 0) = _T7
    return _T6
}

FUNCTION(_Node_New) {
memo ''
_Node_New:
    _T8 = 12
    parm _T8
    _T9 =  call _Alloc
    _T10 = 0
    *(_T9 + 4) = _T10
    *(_T9 + 8) = _T10
    _T11 = VTBL <_Node>
    *(_T9 + 0) = _T11
    return _T9
}

FUNCTION(main) {
memo ''
main:
    _T13 = 7
    _T12 = _T13
    _T15 = 0
    _T16 = (_T12 < _T15)
    if (_T16 == 0) branch _L14
    _T17 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T17
    call _PrintString
    call _Halt
_L14:
    _T18 = 4
    _T19 = (_T18 * _T12)
    _T20 = (_T18 + _T19)
    parm _T20
    _T21 =  call _Alloc
    *(_T21 + 0) = _T12
    _T14 = _T21
    _T23 = 0
    _T22 = _T23
_L15:
    _T24 = (_T22 < _T12)
    if (_T24 == 0) branch _L16
    _T25 =  call _Node_New
    _T26 = *(_T14 + 0)
    _T27 = (_T22 < _T26)
    if (_T27 == 0) branch _L17
    _T28 = 0
    _T29 = (_T22 < _T28)
    if (_T29 == 0) branch _L18
_L17:
    _T30 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T30
    call _PrintString
    call _Halt
_L18:
    _T31 = 4
    _T32 = (_T22 * _T31)
    _T33 = (_T32 + _T31)
    _T34 = *(_T14 + _T33)
    _T35 = 4
    _T36 = (_T22 * _T35)
    _T37 = (_T36 + _T35)
    *(_T14 + _T37) = _T25
    _T38 = *(_T14 + 0)
    _T39 = (_T22 < _T38)
    if (_T39 == 0) branch _L19
    _T40 = 0
    _T41 = (_T22 < _T40)
    if (_T41 == 0) branch _L20
_L19:
    _T42 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T42
    call _PrintString
    call _Halt
_L20:
    _T43 = 4
    _T44 = (_T22 * _T43)
    _T45 = (_T44 + _T43)
    _T46 = *(_T14 + _T45)
    parm _T46
    parm _T22
    _T47 = *(_T46 + 0)
    _T48 = *(_T47 + 12)
    call _T48
    _T49 = 1
    _T50 = (_T22 + _T49)
    _T22 = _T50
    branch _L15
_L16:
    _T51 = 0
    _T22 = _T51
_L21:
    _T52 = (_T22 < _T12)
    if (_T52 == 0) branch _L22
    _T53 = *(_T14 + 0)
    _T54 = (_T22 < _T53)
    if (_T54 == 0) branch _L23
    _T55 = 0
    _T56 = (_T22 < _T55)
    if (_T56 == 0) branch _L24
_L23:
    _T57 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T57
    call _PrintString
    call _Halt
_L24:
    _T58 = 4
    _T59 = (_T22 * _T58)
    _T60 = (_T59 + _T58)
    _T61 = *(_T14 + _T60)
    _T62 = 2
    _T63 = (_T22 * _T62)
    _T64 = 0
    _T65 = (_T12 == _T64)
    if (_T65 == 0) branch _L25
    _T66 = "Decaf runtime error: Division by zero error."
    parm _T66
    call _PrintString
    call _Halt
_L25:
    _T67 = (_T63 % _T12)
    _T68 = *(_T14 + 0)
    _T69 = (_T67 < _T68)
    if (_T69 == 0) branch _L26
    _T70 = 0
    _T71 = (_T67 < _T70)
    if (_T71 == 0) branch _L27
_L26:
    _T72 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T72
    call _PrintString
    call _Halt
_L27:
    _T73 = 4
    _T74 = (_T67 * _T73)
    _T75 = (_T74 + _T73)
    _T76 = *(_T14 + _T75)
    parm _T61
    parm _T76
    _T77 = *(_T61 + 0)
    _T78 = *(_T77 + 8)
    call _T78
    _T79 = 1
    _T80 = (_T22 + _T79)
    _T22 = _T80
    branch _L21
_L22:
    _T82 = 1
    _T83 = *(_T14 + 0)
    _T84 = (_T82 < _T83)
    if (_T84 == 0) branch _L28
    _T85 = 0
    _T86 = (_T82 < _T85)
    if (_T86 == 0) branch _L29
_L28:
    _T87 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T87
    call _PrintString
    call _Halt
_L29:
    _T88 = 4
    _T89 = (_T82 * _T88)
    _T90 = (_T89 + _T88)
    _T91 = *(_T14 + _T90)
    _T81 = _T91
    _T92 = 1
    _T93 = 0
    _T94 = (_T92 < _T93)
    if (_T94 == 0) branch _L30
    _T95 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T95
    call _PrintString
    call _Halt
_L30:
    _T96 = 4
    _T97 = (_T96 * _T92)
    _T98 = (_T96 + _T97)
    parm _T98
    _T99 =  call _Alloc
    *(_T99 + 0) = _T92
    _T14 = _T99
    parm _T81
    _T100 = *(_T81 + 0)
    _T101 = *(_T100 + 16)
    _T102 =  call _T101
    parm _T102
    call _PrintInt
}

FUNCTION(_Node.setNext) {
memo '_T0:4 _T1:8'
_Node.setNext:
    _T103 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_Node.setId) {
memo '_T2:4 _T3:8'
_Node.setId:
    _T104 = *(_T2 + 8)
    *(_T2 + 8) = _T3
}

FUNCTION(_Node.count) {
memo '_T4:4'
_Node.count:
    _T106 = *(_T4 + 4)
    _T105 = _T106
    _T108 = 1
    _T107 = _T108
_L31:
    _T109 = *(_T105 + 8)
    _T110 = *(_T4 + 8)
    _T111 = (_T109 != _T110)
    if (_T111 == 0) branch _L32
    _T112 = *(_T105 + 4)
    _T105 = _T112
    _T113 = 1
    _T114 = (_T107 + _T113)
    _T107 = _T114
    branch _L31
_L32:
    return _T107
}

