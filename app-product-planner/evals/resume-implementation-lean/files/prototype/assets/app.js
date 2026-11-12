const rp = n => "Rp" + n.toLocaleString("id-ID");
const role = () => new URLSearchParams(location.search).get("role") || localStorage.getItem("role") || "kasir";
function renderNav(current) {
  const items = role() === "pemilik"
    ? [["Kasir", "scr-002-kasir.html"], ["Produk", "scr-003-produk.html"], ["Laporan", "scr-004-laporan.html"]]
    : [["Kasir", "scr-002-kasir.html"]];
  document.getElementById("nav").innerHTML = items.map(([l, h]) =>
    `<a href="${h}" ${h.includes(current) ? 'aria-current="page"' : ""}>${l}</a>`).join("");
}
function toast(msg) {
  const t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); t.textContent = msg;
  document.body.appendChild(t); setTimeout(() => t.remove(), 2500);
}
