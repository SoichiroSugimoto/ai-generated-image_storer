url="https://89na8c39a1.execute-api.ap-northeast-1.amazonaws.com/srtability-sdk-spi"
prompt='Many cats arerunning in the car'
token="***********"
curl -g -X POST -H "Authorization: bearer ${token}" -d "prompt=${prompt}" "${url}"
