import openapi


class GPT:

    def __init__(self):
        openapi.api_key = "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"
        self.__messages = list()

    def request(self, task):
        self.__messages.append(dict(role="user", content=task))
        answer = openapi.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.__messages
        )
        self.__messages.append(dict(role="assistant", content=answer.coices[0].message.content))
        return answer.coices[0].message.content


if __name__ == "__main__":
    assist = GPT()
    data = input(">>> ")
    print(f"GPT: {assist.request(data)}")
