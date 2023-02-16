url="https://89na8c39a1.execute-api.ap-northeast-1.amazonaws.com/srtability-sdk-spi"
prompt='Many%20cats%20arerunning%20in%20the%20car'
token="***********"
curl -g -X POST -H "Authorization: bearer ${token}" "${url}?prompt=${prompt}"
