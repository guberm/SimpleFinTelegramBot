namespace SimpleFinBot.Configuration;

public class BotSettings
{
    public TelegramBotSettings TelegramBot { get; set; } = new();
    public DatabaseSettings Database { get; set; } = new();
}

public class TelegramBotSettings
{
    public string BotToken { get; set; } = string.Empty;
}

public class DatabaseSettings
{
    public string ConnectionString { get; set; } = "Data Source=simplefin_multi_accounts.db";
}
