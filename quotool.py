import streamlit as st
import math

def calculate_price(
    cost_price,
    promotion_rate,
    tariff_rate,
    accessories_cost,
    quantity
):
    # 固定值
    insurance_fee_rate = 0.03
    profit_margin = 0.3
    exchange_rate = 7.3

    insurance_fee = cost_price * insurance_fee_rate
    promotion = cost_price * promotion_rate
    tariff = cost_price * tariff_rate

    total_cost = cost_price + insurance_fee + promotion + tariff + accessories_cost
    cny_unit_price = total_cost * (1 + profit_margin)
    usd_unit_price = cny_unit_price / exchange_rate

    usd_total_price = usd_unit_price * quantity if quantity > 0 else 0

    return {
        "总采购成本": round(total_cost, 4),
        "人民币总价": round(cny_unit_price, 4),
        "美元单价": round(usd_unit_price, 4),
        "美元总价": round(usd_total_price, 4) if quantity > 0 else "-"
    }

st.set_page_config(page_title="报价系统", layout="wide")
st.title("🧮 报价系统 (Quotation Tool)")
st.markdown("此工具用于快速计算商品总成本与售价。\n\n**固定值：**\n- 汇率: 7.3\n- 信保手续费: 3%\n- 利润率: 30%")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    cost_price = st.number_input("采购成本 (元)", value=0.0, step=0.01)
    promotion_rate = st.number_input("促销 (%)", value=0.0, step=0.1) / 100

with col2:
    tariff_rate = st.number_input("关税 (%)", value=0.0, step=0.1) / 100
    accessories_cost = st.number_input("配件成本 (元)", value=0.0, step=0.1)

with col3:
    quantity = st.number_input("件数", value=0.0, step=1.0)

st.markdown("---")

if st.button("📊 开始计算"):
    result = calculate_price(
        cost_price,
        promotion_rate,
        tariff_rate,
        accessories_cost,
        quantity
    )

    st.subheader("📈 计算结果：")
    for label, value in result.items():
        st.write(f"**{label}**: {value}")
else:
    st.info("请填写所有必填项并点击“开始计算”按钮。")
