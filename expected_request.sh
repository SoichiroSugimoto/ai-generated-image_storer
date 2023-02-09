$url="https://xxxxxxxxxxxxxxxx"
$prompt="xxxxxxxxxxxxxxxx"
$TOKEN="***********"
curl -g -X POST -H "Authorization: bearer $TOKEN" "$url?prompt=$prompt"