$keyword = Read-Host -Prompt "Enter the search keyword"
$location = Read-Host -Prompt "Enter the search location"
Set-Location -Path "$location"
Get-ChildItem *.pptx |ForEach-Object {
    $NewName = $keyword + " " + $_.LastWriteTime.toString("yyyy-MM-dd-HH-mm")+($script:i++) + ".pptx"
    $Destination = Join-Path -Path $_.Directory.FullName -ChildPath $NewName
    Move-Item -Path $_.FullName -Destination $Destination -Force
}
Write-Host "Done!" -ForegroundColor Green
Read-Host -Prompt "Press Enter to exit"
