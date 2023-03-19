#rakumart_order_all_cost

|  name                      |  date_type          |  length  |  pk    |  not_null |  default           |  comment        |
| ---------------------------|---------------------|----------|--------|-----------|--------------------|-----------------|
|  purchase_order_id         |  integer            |  -       |  true  |  true     |  -                 |  注文書ID        |
|  purchase_order_name       |  character varying  |  100     |  -     |  true     |  -                 |  注文書名         |
|  jpy_equivalent            |  integer            |  -       |  -     |  -        |  -                 |  商品金額(日本円)  |
|  domestic_postage          |  integer            |  -       |  -     |  -        |  -                 |  国内送料(日本円)  |
|  international_postage     |  integer            |  -       |  -     |  -        |  -                 |  国際送料(日本円)  |
|  commision                 |  integer            |  -       |  -     |  -        |  -                 |  手数料           |
|  tariff                    |  integer            |  -       |  -     |  -        |  -                 |  関税            |
|  order_product_total_price |  integer            |  -       |  -     |  -        |  -                 |  注文商品合計金額  |
|  created_at                |  date_time          |  -       |  -     |  true     |  create_timestamp  |  作成日時         |
|  updated_at                |  date_time          |  -       |  -     |  true     |  update_timestamp  |  更新日時         |
|  is_detelted               |  boolean            |  -       |  -     |  true     |  False             |  削除フラグ       |