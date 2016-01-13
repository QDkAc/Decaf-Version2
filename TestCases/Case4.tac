VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_Node) {
    <empty>
    Node
    _Node.setId;
    _Node.count;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T3 = 4
    parm _T3
    _T4 =  call _Alloc
    _T5 = VTBL <_Main>
    *(_T4 + 0) = _T5
    return _T4
}

FUNCTION(_Node_New) {
memo ''
_Node_New:
    _T6 = 8
    parm _T6
    _T7 =  call _Alloc
    _T8 = 0
    *(_T7 + 4) = _T8
    _T9 = VTBL <_Node>
    *(_T7 + 0) = _T9
    return _T7
}

FUNCTION(main) {
memo ''
main:
    _T11 = 7
    _T10 = _T11
    _T13 = 0
    _T14 = (_T10 < _T13)
    if (_T14 == 0) branch _L13
    _T15 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T15
    call _PrintString
    call _Halt
_L13:
    _T16 = 4
    _T17 = (_T16 * _T10)
    _T18 = (_T16 + _T17)
    parm _T18
    _T19 =  call _Alloc
    *(_T19 + 0) = _T10
    _T12 = _T19
    _T21 = 0
    _T20 = _T21
_L14:
    _T22 = (_T20 < _T10)
    if (_T22 == 0) branch _L15
    _T23 =  call _Node_New
    _T24 = *(_T12 + 0)
    _T25 = (_T20 < _T24)
    if (_T25 == 0) branch _L16
    _T26 = 0
    _T27 = (_T20 < _T26)
    if (_T27 == 0) branch _L17
_L16:
    _T28 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T28
    call _PrintString
    call _Halt
_L17:
    _T29 = 4
    _T30 = (_T20 * _T29)
    _T31 = (_T30 + _T29)
    _T32 = *(_T12 + _T31)
    _T33 = 4
    _T34 = (_T20 * _T33)
    _T35 = (_T34 + _T33)
    *(_T12 + _T35) = _T23
    _T36 = *(_T12 + 0)
    _T37 = (_T20 < _T36)
    if (_T37 == 0) branch _L18
    _T38 = 0
    _T39 = (_T20 < _T38)
    if (_T39 == 0) branch _L19
_L18:
    _T40 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T40
    call _PrintString
    call _Halt
_L19:
    _T41 = 4
    _T42 = (_T20 * _T41)
    _T43 = (_T42 + _T41)
    _T44 = *(_T12 + _T43)
    parm _T44
    parm _T20
    _T45 = *(_T44 + 0)
    _T46 = *(_T45 + 8)
    call _T46
    _T47 = 1
    _T48 = (_T20 + _T47)
    _T20 = _T48
    branch _L14
_L15:
    _T50 = 1
    _T51 = *(_T12 + 0)
    _T52 = (_T50 < _T51)
    if (_T52 == 0) branch _L20
    _T53 = 0
    _T54 = (_T50 < _T53)
    if (_T54 == 0) branch _L21
_L20:
    _T55 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T55
    call _PrintString
    call _Halt
_L21:
    _T56 = 4
    _T57 = (_T50 * _T56)
    _T58 = (_T57 + _T56)
    _T59 = *(_T12 + _T58)
    _T49 = _T59
    _T60 = 1
    _T61 = 0
    _T62 = (_T60 < _T61)
    if (_T62 == 0) branch _L22
    _T63 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T63
    call _PrintString
    call _Halt
_L22:
    _T64 = 4
    _T65 = (_T64 * _T60)
    _T66 = (_T64 + _T65)
    parm _T66
    _T67 =  call _Alloc
    *(_T67 + 0) = _T60
    _T12 = _T67
    parm _T49
    _T68 = *(_T49 + 0)
    _T69 = *(_T68 + 12)
    _T70 =  call _T69
    parm _T70
    call _PrintInt
}

FUNCTION(_Node.setId) {
memo '_T0:4 _T1:8'
_Node.setId:
    _T71 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_Node.count) {
memo '_T2:4'
_Node.count:
    _T72 = *(_T2 + 4)
    return _T72
}

