$BasicForeignKey = {
    $NamedArgs = $Args[0]

    $Args | %{Write-Debug "FK Arg - $_"} 

    write-Debug ("Getting reference ($($NamedArgs['outputkey'])) of " + `
                  "$($NamedArgs['lookup_value']) in " + `
                  "$($NamedArgs['lookupdatabase']).$($NamedArgs['lookuptable']) on " + ` 
                  "$($NamedArgs['oldkey']) = $($NamedArgs['newkey'])")
    $Conditions = "WHERE $($NamedArgs['newkey']) = ""$($NamedArgs['lookup_value'])"""
    $Connection = Get-MySqlConnection $NamedArgs['Creds'] $NamedArgs['Server'] $NamedArgs['lookupdatabase']
    $Connection.open()
    (Get-MySqlRows $Connection $NamedArgs['lookupdatabase'] $NamedArgs['lookuptable'] $Conditions)."$($NamedArgs['outputkey'])"
    $Connection.close()
}

$BasicForeignKeyPopulateNulls = {
    $NamedArgs = $Args[0]

    $Args | %{Write-Debug "FK Arg - $_"} 

    write-Debug ("Getting reference ($($NamedArgs['outputkey'])) of " + `
                  "$($NamedArgs['lookup_value']) in " + `
                  "$($NamedArgs['lookupdatabase']).$($NamedArgs['lookuptable']) on " + ` 
                  "$($NamedArgs['oldkey']) = $($NamedArgs['newkey'])")
    $Conditions = "WHERE $($NamedArgs['newkey']) = ""$($NamedArgs['lookup_value'])"""
    $Connection = Get-MySqlConnection $NamedArgs['Creds'] $NamedArgs['Server'] $NamedArgs['lookupdatabase']
    $Connection.open()
    $FK = (Get-MySqlRows $Connection $NamedArgs['lookupdatabase'] $NamedArgs['lookuptable'] $Conditions)."$($NamedArgs['outputkey'])"
    $Connection.close()
    if ($FK -eq $null)
    {
        Write-Debug "ForiegnKey does not exist, creating it"
        $FK = invoke-command -scriptblock $NamedArgs["CreateKey"] -argumentlist $Args -verbose 
    }
    $FK 
}

$CreateIP = {
    $NamedArgs = $Args[0]
    $IPString = $NamedArgs['lookup_value']
    Write-Debug "IP String - $IPString"
    $IPParsed = [system.net.ipaddress]::Parse($IPString).MapToIPv6().ToString();

    $ColumnNames = @("ip","name","comment","reserved","oldip")
    $ColumnData = @($IPParsed,$null,$null,0,$NamedArgs['lookup_value'])

    $Conditions = "WHERE $($NamedArgs['newkey']) = ""$($NamedArgs['lookup_value'])"""

    $Connection = Get-MySqlConnection $NamedArgs['Creds'] $NamedArgs['Server'] $NamedArgs['lookupdatabase']
    $Connection.open()
    
    $ignore = Invoke-MySqlInsert $Connection $NamedArgs['lookupdatabase'] $NamedArgs['lookuptable'] $ColumnNames $ColumnData
    (Get-MySqlRows $Connection $NamedArgs['lookupdatabase'] $NamedArgs['lookuptable'] $Conditions)."$($NamedArgs['outputkey'])"
    $Connection.close()
}

$BasicBoolean = {
    $Bool = $args[0]['lookup_value']
    Write-Debug "Boolean String - $Bool"
    switch ($args[0]['lookup_value'])
    {
        'yes'{'0x1'}
        'no'{'0x0'}
    }
}    

$ParseIP = {
    $IPString = $args[0]['lookup_value']
    Write-Debug "IP String - $IPString"
    [system.net.ipaddress]::Parse($IPString).MapToIPv6().ToString();
}

$ParseProtocol = {
    $PS = $args[0]['lookup_value']
    Write-Debug "Protocol String - $AtomDeets"
    switch ($PS)
    {
        'TCP'{'0x1'}
        'UDP'{'0x2'}
        'MARK'{'0x4'}
    }
}

$ParseAllocation = {
    $Alloc = $($args[0]['lookup_value'])
    Write-Debug "Allocation is $Alloc"
    switch ($Alloc)
    {
        'regular'{1}
        'shared'{2}
        'virtual'{3}
        'router'{4}
        'point2point'{5}
        'sharedrouter'{6}
    }
}

$ParseAtom = {
    $AtomDeets = $args[0]['lookup_value']
    Write-Debug "Atom - $AtomDeets"
    $z = 0
    foreach ($Atom in $AtomDeets)
    {
        switch ($Atom.atom)
        {
            "front" {$z += 1}
            "interior" {$z += 2}
            "rear" {$z += 4}
        }
    }
    $z
}

$ParseDate = {
    $ParseString = $($args[0]['lookup_value'])
    Write-Debug "Date String to parse $ParseString"
    $DTS = (get-date $ParseString).ToString("yyyy/MM/dd HH:mm:ss.FFFFFF")
    Write-Debug "Date Time String output $DTS"
    $DTS
}