using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Server1.Models;
using System.Net.Http;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Text;

namespace Server1.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class Server1Controller : ControllerBase
    {

        [HttpPost]
        [Route("calculate")]
        public async Task<string> Calculate([FromBody] Data requestData)
        {

            HttpClient client = new HttpClient();

            //For HTTP-GET
            //HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Post, "http://127.0.0.1:4444/server2/calculate");
            //request.Headers.Add("Content-Type", "text/json");
            //client.SendAsync(request)

            requestData.Number = requestData.Number * 2;
            
            System.Console.WriteLine("##############");
            System.Console.WriteLine(JsonSerializer.Serialize(requestData));

            HttpContent content = new StringContent(JsonSerializer.Serialize(requestData), Encoding.UTF8, "application/json");

            HttpResponseMessage reponse = await client.PostAsync("http://127.0.0.1:4444/server2/calculate/django/dynamic", content);
            
            System.Console.WriteLine(reponse.Content);

            return await reponse.EnsureSuccessStatusCode().Content.ReadAsStringAsync();
        }
    }

}