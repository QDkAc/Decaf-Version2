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
    _T8 = _T16
    _T17 =  call _Item_New
    _T18 = 0
    _T19 = *(_T8 + 0)
    _T20 = (_T18 < _T19)
    if (_T20 == 0) branch _L13
    _T21 = 0
    _T22 = (_T18 < _T21)
    if (_T22 == 0) branch _L14
_L13:
    _T23 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T23
    call _PrintString
    call _Halt
_L14:
    _T24 = 4
    _T25 = (_T18 * _T24)
    _T26 = (_T25 + _T24)
    _T27 = *(_T8 + _T26)
    _T28 = 4
    _T29 = (_T18 * _T28)
    _T30 = (_T29 + _T28)
    *(_T8 + _T30) = _T17
    _T31 = 0
    _T32 = *(_T8 + 0)
    _T33 = (_T31 < _T32)
    if (_T33 == 0) branch _L15
    _T34 = 0
    _T35 = (_T31 < _T34)
    if (_T35 == 0) branch _L16
_L15:
    _T36 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T36
    call _PrintString
    call _Halt
_L16:
    _T37 = 4
    _T38 = (_T31 * _T37)
    _T39 = (_T38 + _T37)
    _T40 = *(_T8 + _T39)
    _T41 = 5
    parm _T40
    parm _T41
    _T42 = *(_T40 + 0)
    _T43 = *(_T42 + 8)
    _T44 =  call _T43
    _T8 = _T44
}

FUNCTION(_Item.sequence) {
memo '_T0:4 _T1:8'
_Item.sequence:
    _T45 = 0
    _T46 = (_T1 < _T45)
    if (_T46 == 0) branch _L17
    _T47 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T47
    call _PrintString
    call _Halt
_L17:
    _T48 = 4
    _T49 = (_T48 * _T1)
    _T50 = (_T48 + _T49)
    parm _T50
    _T51 =  call _Alloc
    *(_T51 + 0) = _T1
    return _T51
}

