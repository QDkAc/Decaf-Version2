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
    _T8 = VTBL <_Node>
    *(_T7 + 0) = _T8
    return _T7
}

FUNCTION(main) {
memo ''
main:
    _T10 = 7
    _T9 = _T10
    _T12 = 0
    _T13 = (_T9 < _T12)
    if (_T13 == 0) branch _L13
    _T14 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T14
    call _PrintString
    call _Halt
_L13:
    _T15 = 4
    _T16 = (_T15 * _T9)
    _T17 = (_T15 + _T16)
    parm _T17
    _T18 =  call _Alloc
    *(_T18 + 0) = _T9
    _T11 = _T18
    _T20 = 0
    _T19 = _T20
_L14:
    _T21 = (_T19 < _T9)
    if (_T21 == 0) branch _L15
    _T22 =  call _Node_New
    _T23 = *(_T11 + 0)
    _T24 = (_T19 < _T23)
    if (_T24 == 0) branch _L16
    _T25 = 0
    _T26 = (_T19 < _T25)
    if (_T26 == 0) branch _L17
_L16:
    _T27 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T27
    call _PrintString
    call _Halt
_L17:
    _T28 = 4
    _T29 = (_T19 * _T28)
    _T30 = (_T29 + _T28)
    _T31 = *(_T11 + _T30)
    _T32 = 4
    _T33 = (_T19 * _T32)
    _T34 = (_T33 + _T32)
    *(_T11 + _T34) = _T22
    _T35 = *(_T11 + 0)
    _T36 = (_T19 < _T35)
    if (_T36 == 0) branch _L18
    _T37 = 0
    _T38 = (_T19 < _T37)
    if (_T38 == 0) branch _L19
_L18:
    _T39 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T39
    call _PrintString
    call _Halt
_L19:
    _T40 = 4
    _T41 = (_T19 * _T40)
    _T42 = (_T41 + _T40)
    _T43 = *(_T11 + _T42)
    parm _T43
    parm _T19
    _T44 = *(_T43 + 0)
    _T45 = *(_T44 + 8)
    call _T45
    _T46 = 1
    _T47 = (_T19 + _T46)
    _T19 = _T47
    branch _L14
_L15:
    _T49 = 1
    _T50 = *(_T11 + 0)
    _T51 = (_T49 < _T50)
    if (_T51 == 0) branch _L20
    _T52 = 0
    _T53 = (_T49 < _T52)
    if (_T53 == 0) branch _L21
_L20:
    _T54 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T54
    call _PrintString
    call _Halt
_L21:
    _T55 = 4
    _T56 = (_T49 * _T55)
    _T57 = (_T56 + _T55)
    _T58 = *(_T11 + _T57)
    _T48 = _T58
    _T59 = 1
    _T60 = 0
    _T61 = (_T59 < _T60)
    if (_T61 == 0) branch _L22
    _T62 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T62
    call _PrintString
    call _Halt
_L22:
    _T63 = 4
    _T64 = (_T63 * _T59)
    _T65 = (_T63 + _T64)
    parm _T65
    _T66 =  call _Alloc
    *(_T66 + 0) = _T59
    _T11 = _T66
    parm _T48
    _T67 = *(_T48 + 0)
    _T68 = *(_T67 + 12)
    _T69 =  call _T68
    parm _T69
    call _PrintInt
}

FUNCTION(_Node.setId) {
memo '_T0:4 _T1:8'
_Node.setId:
    _T70 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_Node.count) {
memo '_T2:4'
_Node.count:
    _T71 = *(_T2 + 4)
    return _T71
}

