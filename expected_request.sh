url="https://89na8c39a1.execute-api.ap-northeast-1.amazonaws.com/srtability-sdk-spi"
prompt='Many cats arerunning in the car'
TOKEN="***********"
curl -g -X POST -H "Authorization: bearer $TOKEN" -d "prompt=$prompt" "$url"