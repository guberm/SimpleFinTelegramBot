using Microsoft.AspNetCore.Mvc;
using Microsoft.Data.Sqlite;

[ApiController]
[Route("api/[controller]")]
public class AccountsController : ControllerBase
{
    private readonly string _dbFile = "simplefin_multi_accounts.db";

    [HttpGet]
    public IActionResult GetBanks([FromQuery] long user_id)
    {
        if (user_id <= 0) return BadRequest("No user_id");
        var banks = new List<object>();
        using var conn = new SqliteConnection($"Data Source={_dbFile}");
        conn.Open();
        var cmd = conn.CreateCommand();
        cmd.CommandText = @"SELECT access_url, bank_name FROM accounts WHERE user_id=@uid";
        cmd.Parameters.AddWithValue("@uid", user_id);
        using var reader = cmd.ExecuteReader();
        while (reader.Read())
        {
            banks.Add(new
            {
                bank_name = reader.GetString(1),
                access_url = reader.GetString(0)
            });
        }
        return Ok(new { banks });
    }
}
