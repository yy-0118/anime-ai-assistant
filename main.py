
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
    temperature=0.8,
)

# 角色设定 —— 你可以换成你喜欢的角色
system_prompt = """你是蒙奇·D·路飞，海贼王的男人！
说话风格：热血、直率、脑子一根筋但重情义，动不动就说要成为海贼王。
语气：口语化、简短有力，偶尔喊"呐~""喂！"。
绝对不打破人设：你不会用书面语，不会说"根据资料显示"这种话。
"""

# 对话历史（初始只有系统 message）
history = [SystemMessage(content=system_prompt)]

print("🏴‍☠️  路飞 AI 启动！输入 'exit' 退出\n")

while True:
    user_input = input("你：").strip()
    if user_input.lower() in ("exit", "quit", "q"):
        print("路飞：喂！下次带肉来啊！拜拜～")
        break

    # 把用户消息追加进历史
    history.append(HumanMessage(content=user_input))

    # 把整个历史发过去（这就是"记忆"）
    response = llm.invoke(history)
    reply = response.content

    print(f"\n路飞：{reply}\n")

    # 把AI回复也追加进历史
    history.append(SystemMessage(content=reply))
    # ↑ 注意：上面这行其实应该是 AIMessage，但为了简化先用这个跑通
