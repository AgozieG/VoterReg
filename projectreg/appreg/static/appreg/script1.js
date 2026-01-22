    // // small reveal-on-scroll
    // const reveals = document.querySelectorAll('.reveal');
    // const observer = new IntersectionObserver(entries => {
    //   entries.forEach(e => {
    //     if (e.isIntersecting) e.target.classList.add('show')
    //   })
    // }, {threshold:0.12});
    // reveals.forEach(r => observer.observe(r));

    // // set year dynamically in Django you'll pass context; this fallback keeps it filled when tested outside Django
    // (function(){
    //   const el = document.querySelector('.copyright');
    //   if (el && !el.textContent.includes('{{ year }}')) return; // assume template will replace
    //   const y = new Date().getFullYear();
    //   el && (el.textContent = `© ${y} Miner Voter Registration — Built for communities`);
    // })();



        // reveal-on-scroll
    const reveals = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('show') })
    }, {threshold:0.12});
    reveals.forEach(r => observer.observe(r));

    // dynamic year fallback
    (function(){
      const el = document.querySelector('.copyright');
      if (el && !el.textContent.includes('{{ year }}')) return;
      const y = new Date().getFullYear();
      el && (el.textContent = `© ${y} Farmer Voter Registration — Built for rural communities`);
    })();