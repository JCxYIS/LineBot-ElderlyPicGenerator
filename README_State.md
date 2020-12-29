# State Info

## 0：一般情況
- `000`：起始 (無狀態)
    - -> 1
- `001`：開始關注 (顯示QuickReply：功能)
    - 開始製作長輩圖 -> 100

## 1：長輩圖生成
- `100`：開始製作長輩圖 (顯示圖文選單：範本s)
    - goupload -> 101
    - TODO pic_N -> 110    
- `101`：上傳圖片 (等待使用者上傳)
    - (有圖片附件) -> 110
- `110`：選擇功能 (QuickReply：添加文字/效果/完成)
    - addText -> 111
    - TODO
    - finish -> 150
- `111`：輸入文字
    - (有文字) -> 112
- `112`：調整文字位置 (顯示圖文選單 上下左右+完成+取消)  
    - TODO up
    - TODO down
    - TODO left
    - TODO right
    - TODO done
    - TODO cancel
- `150`：完成 (QuickReply：直接完成/分享)
    - end
    - share