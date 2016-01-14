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
    _T10 = VTBL <_Node>
    *(_T9 + 0) = _T10
    return _T9
}

FUNCTION(_Main.one) {
memo ''
_Main.one:
    _T12 = 7
    _T11 = _T12
    _T14 = 0
    _T15 = (_T11 < _T14)
    if (_T15 == 0) branch _L15
    _T16 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T16
    call _PrintString
    call _Halt
_L15:
    _T17 = 4
    _T18 = (_T17 * _T11)
    _T19 = (_T17 + _T18)
    parm _T19
    _T20 =  call _Alloc
    *(_T20 + 0) = _T11
    _T13 = _T20
    _T22 = 0
    _T21 = _T22
_L16:
    _T23 = (_T21 < _T11)
    if (_T23 == 0) branch _L17
    _T24 =  call _Node_New
    _T25 = *(_T13 + 0)
    _T26 = (_T21 < _T25)
    if (_T26 == 0) branch _L18
    _T27 = 0
    _T28 = (_T21 < _T27)
    if (_T28 == 0) branch _L19
_L18:
    _T29 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T29
    call _PrintString
    call _Halt
_L19:
    _T30 = 4
    _T31 = (_T21 * _T30)
    _T32 = (_T31 + _T30)
    _T33 = *(_T13 + _T32)
    _T34 = 4
    _T35 = (_T21 * _T34)
    _T36 = (_T35 + _T34)
    *(_T13 + _T36) = _T24
    _T37 = *(_T13 + 0)
    _T38 = (_T21 < _T37)
    if (_T38 == 0) branch _L20
    _T39 = 0
    _T40 = (_T21 < _T39)
    if (_T40 == 0) branch _L21
_L20:
    _T41 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T41
    call _PrintString
    call _Halt
_L21:
    _T42 = 4
    _T43 = (_T21 * _T42)
    _T44 = (_T43 + _T42)
    _T45 = *(_T13 + _T44)
    parm _T45
    parm _T21
    _T46 = *(_T45 + 0)
    _T47 = *(_T46 + 12)
    call _T47
    _T48 = 1
    _T49 = (_T21 + _T48)
    _T21 = _T49
    branch _L16
_L17:
    _T50 = 0
    _T21 = _T50
_L22:
    _T51 = (_T21 < _T11)
    if (_T51 == 0) branch _L23
    _T52 = *(_T13 + 0)
    _T53 = (_T21 < _T52)
    if (_T53 == 0) branch _L24
    _T54 = 0
    _T55 = (_T21 < _T54)
    if (_T55 == 0) branch _L25
_L24:
    _T56 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T56
    call _PrintString
    call _Halt
_L25:
    _T57 = 4
    _T58 = (_T21 * _T57)
    _T59 = (_T58 + _T57)
    _T60 = *(_T13 + _T59)
    _T61 = 2
    _T62 = (_T21 * _T61)
    _T63 = 0
    _T64 = (_T11 == _T63)
    if (_T64 == 0) branch _L26
    _T65 = "Decaf runtime error: Division by zero error."
    parm _T65
    call _PrintString
    call _Halt
_L26:
    _T66 = (_T62 % _T11)
    _T67 = *(_T13 + 0)
    _T68 = (_T66 < _T67)
    if (_T68 == 0) branch _L27
    _T69 = 0
    _T70 = (_T66 < _T69)
    if (_T70 == 0) branch _L28
_L27:
    _T71 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T71
    call _PrintString
    call _Halt
_L28:
    _T72 = 4
    _T73 = (_T66 * _T72)
    _T74 = (_T73 + _T72)
    _T75 = *(_T13 + _T74)
    parm _T60
    parm _T75
    _T76 = *(_T60 + 0)
    _T77 = *(_T76 + 8)
    call _T77
    _T78 = 1
    _T79 = (_T21 + _T78)
    _T21 = _T79
    branch _L22
_L23:
    _T80 = 1
    _T81 = *(_T13 + 0)
    _T82 = (_T80 < _T81)
    if (_T82 == 0) branch _L29
    _T83 = 0
    _T84 = (_T80 < _T83)
    if (_T84 == 0) branch _L30
_L29:
    _T85 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T85
    call _PrintString
    call _Halt
_L30:
    _T86 = 4
    _T87 = (_T80 * _T86)
    _T88 = (_T87 + _T86)
    _T89 = *(_T13 + _T88)
    return _T89
}

FUNCTION(main) {
memo ''
main:
    _T91 =  call _Main.one
    _T90 = _T91
    parm _T90
    _T92 = *(_T90 + 0)
    _T93 = *(_T92 + 16)
    _T94 =  call _T93
    parm _T94
    call _PrintInt
	call _GC
}

FUNCTION(_Node.setNext) {
memo '_T0:4 _T1:8'
_Node.setNext:
    _T95 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_Node.setId) {
memo '_T2:4 _T3:8'
_Node.setId:
    _T96 = *(_T2 + 8)
    *(_T2 + 8) = _T3
}

FUNCTION(_Node.count) {
memo '_T4:4'
_Node.count:
    _T98 = *(_T4 + 4)
    _T97 = _T98
    _T100 = 1
    _T99 = _T100
_L31:
    _T101 = *(_T97 + 8)
    _T102 = *(_T4 + 8)
    _T103 = (_T101 != _T102)
    if (_T103 == 0) branch _L32
    _T104 = *(_T97 + 4)
    _T97 = _T104
    _T105 = 1
    _T106 = (_T99 + _T105)
    _T99 = _T106
    branch _L31
_L32:
    return _T99
}

