$keyword = Read-Host -Prompt "Enter the search keyword"
$location = Read-Host -Prompt "Enter the search location"
Set-Location -Path "$location"
Get-ChildItem | Rename-Item -NewName {$keyword + " " + $_.LastWriteTime.ToString("yyyy-MM-dd HH.mm") + ($_.Extension)}
Write-Host "Done!" -ForegroundColor Green
Read-Host -Prompt "Press Enter to exit"