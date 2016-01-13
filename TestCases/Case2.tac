VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_Item) {
    <empty>
    Item
    _Item.sequence;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T2 = 4
    parm _T2
    _T3 =  call _Alloc
    _T4 = VTBL <_Main>
    *(_T3 + 0) = _T4
    return _T3
}

FUNCTION(_Item_New) {
memo ''
_Item_New:
    _T5 = 4
    parm _T5
    _T6 =  call _Alloc
    _T7 = VTBL <_Item>
    *(_T6 + 0) = _T7
    return _T6
}

FUNCTION(main) {
memo ''
main:
    _T9 = 5
    _T10 = 0
    _T11 = (_T9 < _T10)
    if (_T11 == 0) branch _L12
    _T12 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T12
    call _PrintString
    call _Halt
_L12:
    _T13 = 4
    _T14 = (_T13 * _T9)
    _T15 = (_T13 + _T14)
    parm _T15
    _T16 =  call _Alloc
    *(_T16 + 0) = _T9
    _T17 = 0
    _T18 = 0
_L13:
    _T15 = (_T15 - _T13)
    if (_T15 == 0) branch _L14
    _T18 = (_T18 + _T13)
    *(_T16 + _T18) = _T17
    branch _L13
_L14:
    _T8 = _T16
    _T19 =  call _Item_New
    _T20 = 0
    _T21 = *(_T8 + 0)
    _T22 = (_T20 < _T21)
    if (_T22 == 0) branch _L15
    _T23 = 0
    _T24 = (_T20 < _T23)
    if (_T24 == 0) branch _L16
_L15:
    _T25 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T25
    call _PrintString
    call _Halt
_L16:
    _T26 = 4
    _T27 = (_T20 * _T26)
    _T28 = (_T27 + _T26)
    _T29 = *(_T8 + _T28)
    _T30 = 4
    _T31 = (_T20 * _T30)
    _T32 = (_T31 + _T30)
    *(_T8 + _T32) = _T19
    _T33 = 0
    _T34 = *(_T8 + 0)
    _T35 = (_T33 < _T34)
    if (_T35 == 0) branch _L17
    _T36 = 0
    _T37 = (_T33 < _T36)
    if (_T37 == 0) branch _L18
_L17:
    _T38 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T38
    call _PrintString
    call _Halt
_L18:
    _T39 = 4
    _T40 = (_T33 * _T39)
    _T41 = (_T40 + _T39)
    _T42 = *(_T8 + _T41)
    _T43 = 5
    parm _T42
    parm _T43
    _T44 = *(_T42 + 0)
    _T45 = *(_T44 + 8)
    _T46 =  call _T45
    _T8 = _T46
}

FUNCTION(_Item.sequence) {
memo '_T0:4 _T1:8'
_Item.sequence:
    _T47 = 0
    _T48 = (_T1 < _T47)
    if (_T48 == 0) branch _L19
    _T49 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T49
    call _PrintString
    call _Halt
_L19:
    _T50 = 4
    _T51 = (_T50 * _T1)
    _T52 = (_T50 + _T51)
    parm _T52
    _T53 =  call _Alloc
    *(_T53 + 0) = _T1
    _T54 = 0
    _T55 = 0
_L20:
    _T52 = (_T52 - _T50)
    if (_T52 == 0) branch _L21
    _T55 = (_T55 + _T50)
    *(_T53 + _T55) = _T54
    branch _L20
_L21:
    return _T53
}

