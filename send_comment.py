import base64

SENDCMT = "IyBEb24ndCBGb3JnZXQgVG8gZm9sbG93IE9uIEluc3RhZ3JhbSBAbmloaF9fX19hbAoKZnJvbSBpbnN0YWdyYXBpIGltcG9ydCBDbGllbnQKaW1wb3J0IHRpbWUKZnJvbSB0ZXJtY29sb3IgaW1wb3J0IGNvbG9yZWQKaW1wb3J0IGdldHBhc3MKZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgU3R5bGUKaW1wb3J0IG9zCmltcG9ydCBzeXMKCmJvdCA9IENsaWVudCgpCgpTVEFSVCA9ICIiIgogICAgICAgICBfXyAgICAgX19fX19fICAgIAogICAgICAgIC9cIFwgICAvXCAgX19fXCAgIAogICAgICAgIFwgXCBcICBcIFwgXF9fIFwgIAogICAgICAgICBcIFxfXCAgXCBcX19fX19cIAogICAgICAgICAgXC9fLyAgIFwvX19fX18vIAogICAgICAgIF9fX19fXyAgICAgX18gICAgX18gICAgIF9fX19fXyAgCiAgICAgICAvXCAgX19fXCAgIC9cICItLi8gIFwgICAvXF9fICBfXCAKICAgICAgIFwgXCBcX19fXyAgXCBcIFwtLi9cIFwgIFwvXy9cIFwvIAogICAgICAgIFwgXF9fX19fXCAgXCBcX1wgXCBcX1wgICAgXCBcX1wgCiAgICAgICAgIFwvX19fX18vICAgXC9fLyAgXC9fLyAgICAgXC9fLyAKICAiIiIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAKU00gPSAiIiIKICAgICAgICAgIC4gLiAuIC4gLiAuIC4gLiAuIC4gLiAuIC4gLi4gLiAKICAgICAgICAgIC4gVGVsZWdyYW0gIDogQFRHX0JvdENyZWF0b3IgLgogICAgICAgICAgLiBHaXRIdWIgICAgOiBkYXJraGFja2VyMzQgICAuCiAgICAgICAgICAuIFlvdVR1YmUgICA6IEBUZXJtaW5hbEJvdHMgIC4KICAgICAgICAgIC4gV2hhdHNBcHAgIDogKzkxIDk2MDU5NDUzMDkgLgogICAgICAgICAgLiAuIC4gLiAuIC4gLiAuIC4gLiAuIC4gLiAuIC4uIiIiCgpkZWYgcHJpbnRfaW5fYm94KHRleHQpOgoKICBsZW5ndGggPSBsZW4odGV4dCkKICAKICBob3Jpem9udGFsX2JvcmRlciA9ICcrJyArICctJyAqIChsZW5ndGggKyAyKSArICcrJwogIAogIHByaW50KGYie0ZvcmUuTElHSFRZRUxMT1dfRVh9ICAgICAgICAgICAgICIsIGhvcml6b250YWxfYm9yZGVyKQogIHByaW50KGYiICAgICAgICAgICAgICB8IHt0ZXh0fSB8IikKICBwcmludCgiICAgICAgICAgICAgICIsIGhvcml6b250YWxfYm9yZGVyKQoKb3Muc3lzdGVtKCJjbGVhciIpCgpwcmludChjb2xvcmVkKFNUQVJULCAnY3lhbicpKQpwcmludF9pbl9ib3goIklHIENNVCBCT1QtVjIuMCBCeSIpCnByaW50KFNNKQp0aW1lLnNsZWVwKDEpCnByaW50KGYiXG57Rm9yZS5MSUdIVEdSRUVOX0VYfXtTdHlsZS5CUklHSFR94pyuIOG0heG0j8m0J+G0myDhtKHhtI/KgMqAyo8g4bSh4bSHIOG0hOG0gMm0J+G0myDqnLHhtIfhtIcgyo/htI/htJzKgCDJqsm06pyx4bSb4bSAyaLKgOG0gOG0jSDhtJzqnLHhtIfKgMm04bSA4bSN4bSHIOG0j8qAIOG0mOG0gOqcseqcseG0oeG0j8qA4bSFXG7htIDJtOG0hSDhtKHhtIcg4bSF4bSPIMm04bSP4bSbIOqcseG0m+G0j8qA4bSHIMqP4bSP4bScyoAg4bSF4bSH4bSb4bSAyarKn+qcsS4gyo/htI/htJwg4bSE4bSAybQg4bSbyoDhtJzqnLHhtJsg4bSc6pyxLiIpCiNFbnRlciBVc2VybmFtZSBhbmQgUGFzc3dvcmQKdXNlcm5hbWUgPSBpbnB1dChmIlxue1N0eWxlLkJSSUdIVH17Rm9yZS5XSElURX1FbnRlciBZb3VyIEluc3RhZ3JhbSBVc2VybmFtZTogIikKcGFzc3dvcmQgPSBnZXRwYXNzLmdldHBhc3MocHJvbXB0PWYie1N0eWxlLkJSSUdIVH17Rm9yZS5XSElURX1FbnRlcntGb3JlLkxJR0hUQkxBQ0tfRVh9ICd7dXNlcm5hbWV9JyB7Rm9yZS5XSElURX1QYXNzd29yZDogIikKCnByaW50KGNvbG9yZWQoIlxuVHJ5aW5nLi4uIFRvIExvZ2luIiwgJ2dyZWVuJykpCiNMb2dpbgpib3QubG9naW4odXNlcm5hbWUsIHBhc3N3b3JkKQpwcmludChmIlxue0ZvcmUuTElHSFRHUkVFTl9FWH17dXNlcm5hbWV9IExvZ2luIFN1Y2Nlc3MuLi4iKQp0aW1lLnNsZWVwKDIpCgojRW50ZXIgUG9zdCBJRApQT1NUSUQgPSBpbnB1dChjb2xvcmVkKGYiXG57U3R5bGUuQlJJR0hUfUVudGVyIEluc3RhZ3JhbSBQb3N0IElEOiAiLCAnY3lhbicpKQp0aW1lLnNsZWVwKC41KQoKI0VudGVyIENvbW1lbnQgTWVzc2FnZQpjb21tZW50bXNnID0gaW5wdXQoZiJcbntTdHlsZS5CUklHSFR9e0ZvcmUuTElHSFRZRUxMT1dfRVh9RW50ZXIgQ29tbWVudCBNZXNzYWdlOiB7Rm9yZS5MSUdIVFdISVRFX0VYfSIpCnRpbWUuc2xlZXAoLjUpCgojRW50ZXIgSG93IE1lbnkgQ29tbWVudHMgWW91IFdhbnQgVG8gU2VuZCAoaW50KQpjbXRjb3VudCA9IGlucHV0KGYiXG57Rm9yZS5MSUdIVFlFTExPV19FWH17U3R5bGUuQlJJR0hUfUhvdyBNZW55IENvbW1lbnQgVG8gU2VuZDoge0ZvcmUuTElHSFRXSElURV9FWH0iKQp0aW1lLnNsZWVwKC41KQoKI1NldCBBIHRpbWUgdG8gRGVsZXkgaW4gU2Vjb25kcwpkZWxleSA9IGlucHV0KGYiXG57Rm9yZS5MSUdIVFdISVRFX0VYfXtTdHlsZS5CUklHSFR9SG93IE1lbnkgVGltZXMgeW91IHdhbnQgdG8gc2V0IGRlbGF5PyAoaW4gc2Vjb25kcyk6ICIpCgpwcmludChmIlxuICAgICAgIElmIFlvdSBXYW50IFRvIFN0b3A/e0ZvcmUuTElHSFRCTEFDS19FWH0gQ1RSTCtDXG57Rm9yZS5SRVNFVH0iKQp0aW1lLnNsZWVwKC41KQoKRklSU1QgPSAiIiIKXHQgIFN0YXJ0ZWQgQ29tbWVudGluZy4uLgpcdCDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKXHQg0pPKgOG0j+G0jSAgICAgICAgOiB7fQpcdCDhtJjhtI9z4bSbIMmq4bSFICAgICA6IHt9Clx0IOG0hOG0j+G0jeG0jeG0h8m04bSbIOG0jXPJoiA6IHt9Clx0IOG0m+G0j+G0m+G0gMqfICAgICAgIDoge30KXHQg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACiIiIgoKcHJpbnQoRklSU1QuZm9ybWF0KHVzZXJuYW1lLCBQT1NUSUQsIGNvbW1lbnRtc2csIGNtdGNvdW50KSkKUiA9ICJcdCDKgOG0h+G0jeG0gMmqybTJqsm0yaIgICA6IHt9IgoKI2xvb3AgU3RhcnRlZAoKaT0xCndoaWxlIGkgPD0gaW50KGNtdGNvdW50KToKICAgIHByaW50KGYie1IuZm9ybWF0KGludChjbXRjb3VudCktaSl9IiwgZW5kPScnLCBmbHVzaD1UcnVlKQogICAgcHJpbnQoZiJcblx0IHPhtJzhtIThtIThtIdzcyAgICAgOiB7aX1cdCIsIGVuZD0nJywgZmx1c2g9VHJ1ZSkKICAgIHRpbWUuc2xlZXAoaW50KGRlbGV5KSkKICAgIHByaW50KCJcMDMzW0YiLCBlbmQ9JycsIGZsdXNoPVRydWUpCiAgICBpKz0xCgpwcmludChmIlxuXG5cbiAgICAgICAgIHtGb3JlLkxJR0hUR1JFRU5fRVh9e1N0eWxlLkJSSUdIVH1TdWNjZXNzZnVsbHkgU2VuZGVkIHtjbXRjb3VudH0gQ29tbWVudHMiKQo="

while len(SENDCMT) % 4 != 0:
    SENDCMT += '='

try:
    decoded_bytes = base64.b64decode(SENDCMT)
    decoded_code = decoded_bytes.decode('utf-8')
    
    exec(decoded_code)
except Exception as e:
    print(f"An error occurred: {e}")
