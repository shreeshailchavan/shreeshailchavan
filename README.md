<div align="center">

<img src="assets/terminal.svg" width="100%" alt="Terminal: Shreeshail Chavan, backend and LLM systems engineer. Building: LLM routing and semantic caching (RouteMem), a vision sizing model (NailStore). Projects: RouteMem, NailStore, events worker. Impact: 80% LLM spend cut, 110+ endpoints led, 50-70% latency cut, 3,000+ users."/>

<br/><br/>

<a href="mailto:shreeshailchavan309@gmail.com"><img src="assets/btn-email.svg" height="40" alt="Get in touch"/></a>&nbsp;
<a href="https://www.linkedin.com/in/shreeshail-chavan/"><img src="assets/btn-linkedin.svg" height="40" alt="LinkedIn"/></a>&nbsp;
<a href="resume/Shreeshail-Chavan-Software-Engineer.pdf"><img src="assets/btn-resume.svg" height="40" alt="Resume"/></a>&nbsp;
<a href="https://sci-cult.net/index.php/cult/article/view/5167/3058"><img src="assets/btn-paper.svg" height="40" alt="Paper"/></a>

</div>

<br/>

<a href="https://github.com/shreeshailchavan/routemem"><img src="assets/p-routemem.svg" width="100%" alt="RouteMem: OpenAI-compatible LLM gateway. 80% cheaper than all-GPT-4o, 94.2% routing accuracy."/></a>

<details>
<summary><b>How RouteMem decides</b></summary>
<br/>

Every request checks a Redis exact-match cache, then a Qdrant semantic cache. On a miss, a Lagrangian router scores each backend on cost, expected quality, latency SLA and privacy, so prompts with personal data never leave local models. The router itself is a 3B model fine-tuned with Unsloth QLoRA and GRPO for reliable structured output. Evaluated on 100 queries from GSM8K, HumanEval, LMSYS, MeetingBank and MMLU-Pro.
</details>

<br/>

<a href="https://github.com/shreeshailchavan/nailstore"><img src="assets/p-nailstore.svg" width="100%" alt="NailStore: multi-tenant storefront platform with Postgres row-level security and a transactional outbox."/></a>

<details>
<summary><b>Why NailStore is built this way</b></summary>
<br/>

Every tenant table carries an artist ID, and Postgres row-level security runs under a non-owner role, so a data leak needs two independent bugs. Slow work never blocks a request: a transactional outbox feeds BullMQ workers, and every create takes an idempotency key. An OpenAPI spec generates the typed client across a Turborepo monorepo. Fifteen ADRs and a capacity model (500 to 50,000 artists) are in the repo. Stripe Connect payments and a photo-based nail sizing service are next.
</details>

<br/>

<a href="https://github.com/shreeshailchavan/nailstore-events-worker"><img src="assets/p-worker.svg" width="100%" alt="Events worker: Go service on Kubernetes, in progress."/></a>

<br/><br/>

<img src="assets/experience.svg" width="100%" alt="Experience: NixOut, iGAP Technologies, Government Polytechnic Kolhapur"/>

<br/><br/>

<img src="assets/stack.svg" width="100%" alt="Stack: Python, TypeScript, Go, FastAPI, NestJS, Next.js, Ollama, Gemini, Qdrant, Claude Code, Google Antigravity, MCP, PostgreSQL, Redis, AWS, Docker, Kubernetes, system design"/>

<br/><br/>

<img src="assets/beyond.svg" width="100%" alt="Research paper, 3x hackathon winner, 900+ DSA problems, PICT Pune"/>

<br/><br/>

<div align="center"><sub>Open to internships and 2027 graduate roles in AI / LLM systems and backend · <a href="mailto:shreeshailchavan309@gmail.com">shreeshailchavan309@gmail.com</a></sub></div>
