package main

import (
	"encoding/json"
	"log"
	"os"
	"strings"

	tgbotapi "gopkg.in/telegram-bot-api.v4"
)

type Config struct {
	TelegramBotToken string
	BotanApiToken    string
}

func main() {
	file, _ := os.Open("config.json")
	decoder := json.NewDecoder(file)
	configuration := Config{}
	err := decoder.Decode(&configuration)
	if err != nil {
		log.Panic(err)
	}

	bot, err := tgbotapi.NewBotAPI(configuration.TelegramBotToken)
	if err != nil {
		log.Panic(err)
	}

	bot.Debug = false

	log.Printf("Authorized on account %s", bot.Self.UserName)
	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates, err := bot.GetUpdatesChan(u)
	if err != nil {
		log.Panic(err)
	}
	for update := range updates {
		reply := `Не знаю что сказать. Попробуйти отправить Git. А еще можно отправить Tasks...
        `
		if update.Message == nil {
			continue
		}
		mess := strings.ToLower(update.Message.Text)
		switch mess {
		case "git":
			reply = "https://github.com/vacilyok"
		case "tasks":
			reply = "1. homework01\n2. homework02\n3. homework03"
		case "task01":
			reply = "https://github.com/vacilyok/Andersen-course/tree/master/homework01"
		case "task1":
			reply = "https://github.com/vacilyok/Andersen-course/tree/master/homework01"
		case "task02":
			reply = "https://github.com/vacilyok/Andersen-course/tree/master/homework02"
		case "task2":
			reply = "https://github.com/vacilyok/Andersen-course/tree/master/homework02"
		case "task03":
			reply = "https://github.com/vacilyok/Andersen-course/tree/master/homework03"
		case "task3":
			reply = "https://github.com/vacilyok/Andersen-course/tree/master/homework03"

		}
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, reply)
		bot.Send(msg)
	}

}
